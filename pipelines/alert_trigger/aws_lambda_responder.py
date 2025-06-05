import json
import boto3

def lambda_handler(event, context):
    alert = json.loads(event['body'])
    if alert.get("alert"):
        print("Triggering response: simulate IAM access revoke")
        iam = boto3.client("iam")
        # Simulate alert response (in practice you'd revoke keys or apply tags)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Simulated IAM revoke response for user",
                "user": alert.get("Account")
            })
        }
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "No action taken"})
    }
