def lambda_handler(event, context):
    print("Event:",event)
    return {"statusCode":200, "body":"hello from the container"}
