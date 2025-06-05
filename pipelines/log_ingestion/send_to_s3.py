import boto3
import json

def upload_to_s3(bucket_name, file_path, s3_key):
    s3 = boto3.client("s3")
    with open(file_path, "rb") as f:
        s3.upload_fileobj(f, bucket_name, s3_key)
    print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    upload_to_s3("security-lake-lab-logs", "../../logs/aws_sample.json", "logs/aws_sample.json")