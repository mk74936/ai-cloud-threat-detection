variable "azure_subscription_id" {}
variable "azure_client_id" {}
variable "azure_client_secret" {}
variable "azure_tenant_id" {}
variable "azure_location" {
  default = "East US"
}

variable "aws_region" {
  default = "us-east-1"
}
variable "aws_access_key" {}
variable "aws_secret_key" {}
