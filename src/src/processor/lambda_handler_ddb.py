import os
import json
import boto3
from datetime import datetime, timezone
from urllib.parse import unquote_plus

table = boto3.resource("dynamodb", region_name="ap-south-1").Table(
    os.environ["TABLE_NAME"]
)


def lambda_handler(event, context):
    for sqs_record in event["Records"]:
        body = json.loads(sqs_record["body"])

        if "Records" not in body:
            print("Skipping non-upload message")
            continue

        for s3_record in body["Records"]:
            key = unquote_plus(s3_record["s3"]["object"]["key"])
            size = s3_record["s3"]["object"].get("size", 0)
            tenant = key.split("/")[0]
            now = datetime.now(timezone.utc).isoformat()

            # 1. save the record as UPLOADED
            table.put_item(
                Item={
                    "tenant_id": tenant,
                    "object_key": key,
                    "size_bytes": size,
                    "scan_status": "UPLOADED",
                    "updated_at": now,
                }
            )

            # 2. STUB scan: not a real scan, it just pretends the file is clean
            scan_result = "CLEAN"

            # 3. update the record with the result
            table.update_item(
                Key={"tenant_id": tenant, "object_key": key},
                UpdateExpression="SET scan_status = :s, updated_at = :t",
                ExpressionAttributeValues={
                    ":s": scan_result,
                    ":t": datetime.now(timezone.utc).isoformat(),
                },
            )

            print(f"tenant={tenant} key={key} status={scan_result}")