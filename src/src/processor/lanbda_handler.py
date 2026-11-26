import json
from urllib.parse import unquote_plus

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        if "Records" not in body:
            print("Skipping non-upload message")
            continue

        for s3_record in body["Records"]:
            key = unquote_plus(s3_record["s3"]["object"]["key"])
            size = s3_record["s3"]["object"].get("size")
            tenant = key.split("/")[0]
            print(f"tenant={tenant} key={key} size={size}")