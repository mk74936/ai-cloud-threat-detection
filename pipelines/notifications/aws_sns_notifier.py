import boto3
import json

def notify(topic_arn, message):
    sns = boto3.client("sns")
    response = sns.publish(
        TopicArn=topic_arn,
        Message=json.dumps({"default": message}),
        Subject="Security Alert",
        MessageStructure="json"
    )
    print("Notification sent:", response)

if __name__ == "__main__":
    notify("arn:aws:sns:us-west-2:123456789012:SecurityAlerts", "🚨 AWS Alert: Unusual login detected.")
