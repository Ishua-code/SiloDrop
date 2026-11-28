import json
import os
import subprocess
from datetime import datetime, timezone
from urllib.parse import unquote_plus

import boto3

MAX_FILE_SIZE = 50 * 1024 * 1024      # 50 MB: write your reason in design-decisions.md
TEMP_FILE = "/tmp/scan-target"
SCAN_TIMEOUT = 100                    # CHANGED: below the 120 s function timeout
LOCAL_TEST = os.environ.get("LOCAL_TEST") == "1"   # CHANGED: replaces commenting code in/out

if not LOCAL_TEST:                    # CHANGED: no AWS clients needed for local testing
    s3 = boto3.client("s3")
    table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])  # CHANGED: env var


def parse_signature(stdout):
    # Line looks like: "/tmp/scan-target: Eicar-Test-Signature FOUND"
    for line in stdout.splitlines():
        if line.endswith(" FOUND"):
            # CHANGED: split on the first ": " only, then drop the suffix
            return line.split(": ", 1)[1].removesuffix(" FOUND")
    return None


def scan(bucket, key):
    try:
        if not LOCAL_TEST:
            s3.download_file(bucket, key, TEMP_FILE)   # CHANGED: restored

        result = subprocess.run(
            ["clamscan", TEMP_FILE],
            capture_output=True,
            text=True,
            timeout=SCAN_TIMEOUT,
        )

        if result.returncode == 0:
            return "CLEAN", None
        if result.returncode == 1:
            return "INFECTED", parse_signature(result.stdout)
        raise RuntimeError(f"ClamAV failed, exit={result.returncode}: {result.stderr}")
    finally:
        if os.path.exists(TEMP_FILE) and not LOCAL_TEST:
            os.remove(TEMP_FILE)


def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        if "Records" not in body:
            print("Skipping non-upload message")
            continue

        for s3_record in body["Records"]:
            bucket = s3_record["s3"]["bucket"]["name"]
            key = unquote_plus(s3_record["s3"]["object"]["key"])
            size = s3_record["s3"]["object"].get("size")
            tenant = key.split("/")[0]
            print(f"tenant={tenant} key={key} size={size}")

            if size is None:
                raise ValueError("Missing object size")

            if size > MAX_FILE_SIZE:
                status, signature = "REJECTED_TOO_LARGE", None
            else:
                status, signature = scan(bucket, key)

            if LOCAL_TEST:
                print(f"LOCAL_TEST: would write status={status} signature={signature}")
                continue

            table.update_item(
                Key={"tenant_id": tenant, "object_key": key},
                UpdateExpression="SET #s = :s, signature = :sig, scanned_at = :t",
                ExpressionAttributeNames={"#s": "status"},
                ExpressionAttributeValues={
                    ":s": status,
                    ":sig": signature,
                    ":t": datetime.now(timezone.utc).isoformat(),
                },
            )
            print(f"DynamoDB updated: tenant={tenant} status={status}")

    return {"statusCode": 200, "body": "Scanning completed"}