import json

def lambda_handler(event, context):
    log = json.loads(event['body'])
    print("Received log:", log)

    # Dummy scoring logic
    if log.get("EventName") == "ConsoleLogin" and log.get("SourceIP") == "203.0.113.0":
        return {
            "statusCode": 200,
            "body": json.dumps({"alert": True, "reason": "Suspicious login from unknown IP"})
        }
    return {
        "statusCode": 200,
        "body": json.dumps({"alert": False})
    }
