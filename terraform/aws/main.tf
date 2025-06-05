provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "logs_bucket" {
  bucket = "security-lake-lab-logs"
  force_destroy = true
}

resource "aws_security_lake" "default" {
  auto_enable = true
  configuration {
    region = "us-west-2"
    sources = ["CLOUD_TRAIL"]
  }
}
