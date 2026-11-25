import json

def lambda_handler(event, context):
    print("Received event:",json.dumps(event))
    tenant=event.get("tenant_id","unknown")
    return {"statusCode": 200, "body": f"helo {tenant}"}

