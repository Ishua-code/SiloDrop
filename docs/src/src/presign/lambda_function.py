import os
import json
import boto3
from botocore.config import Config

s3 = boto3.client("s3", region_name="ap-south-1",
                  config=Config(signature_version="s3v4"))
BUCKET = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):
    tenant = event["tenant_id"]
    filename = event["filename"]

    key = f"{tenant}/{filename}"

    url = s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": BUCKET, "Key": key},
        ExpiresIn=60,
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"upload_url": url}),
    }