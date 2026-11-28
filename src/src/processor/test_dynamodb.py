import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("silodrop-documents")

table.update_item(
    Key={
        "tenant_id": "tenant-123",
        "object_key": "tenant-123/test-file.pdf"
    },
    UpdateExpression="""
        SET #status = :status,
            signature = :signature,
            scanned_at = :timestamp
    """,
    ExpressionAttributeNames={
        "#status": "status"
    },
    ExpressionAttributeValues={
        ":status": "CLEAN",
        ":signature": None,
        ":timestamp": datetime.now(timezone.utc).isoformat()
    }
)

print("DynamoDB update successful!")