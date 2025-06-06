import boto3
import os

def upload_to_s3(bucket_name, file_path, s3_key):
    s3 = boto3.client("s3")
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, bucket_name, s3_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    log_path = os.path.join(current_dir, "..", "..", "logs", "aws_test.json")
    upload_to_s3("security-lake-lab-logs", log_path, "logs/aws_test.json")
