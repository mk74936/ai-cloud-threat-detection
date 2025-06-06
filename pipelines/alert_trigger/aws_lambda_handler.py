import json

def lambda_handler(event, context):
    # API Gateway passes the body as a JSON string. Handle both string
    # and dict payloads for easier local testing.
    if isinstance(event.get("body"), str):
        log = json.loads(event["body"])
    else:
        log = event.get("body", {})
    print("Received log:", log)

    # Dummy scoring logic
    # CloudTrail logs use 'eventName' and 'sourceIPAddress' keys
    if (
        log.get("eventName") == "ConsoleLogin"
        and log.get("sourceIPAddress") == "203.0.113.0"
    ):
        return {
            "statusCode": 200,
            "body": json.dumps({"alert": True, "reason": "Suspicious login from unknown IP"})
        }
    return {
        "statusCode": 200,
        "body": json.dumps({"alert": False})
    }
