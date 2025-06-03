terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.0"
    }
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }

  backend "local" {
    path = "terraform.tfstate"
  }
}

provider "azurerm" {
  alias           = "azure"
  subscription_id = var.azure_subscription_id
  client_id       = var.azure_client_id
  client_secret   = var.azure_client_secret
  tenant_id       = var.azure_tenant_id
}

provider "aws" {
  alias   = "aws"
  region  = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "azurerm_resource_group" "main" {
  provider = azurerm.azure
  name     = "cloud-threat-rg"
  location = var.azure_location
}

resource "azurerm_log_analytics_workspace" "sentinel_workspace" {
  provider            = azurerm.azure
  name                = "sentinel-workspace"
  location            = var.azure_location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "aws_s3_bucket" "security_logs_bucket" {
  provider = aws.aws
  bucket   = "cloud-threat-detection-logs-${random_id.bucket_id.hex}"

  tags = {
    Name        = "Security Logs"
    Environment = "Dev"
  }
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_security_lake" "main" {
  enable_all_regions = true
}

resource "aws_security_lake_subscriber" "example" {
  name              = "ml-threat-detection"
  account_id        = var.aws_account_id
  external_id       = "external-id-for-cross-account-if-any"
  source_type       = "CUSTOM"
  source_details {
    source_name = "threat-model"
    source_version = "1"
  }
}

resource "azurerm_log_analytics_workspace" "sentinel_workspace" {
  name                = "sentinel-log-analytics"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_sentinel_alert_rule_scheduled" "example_rule" {
  name                       = "suspicious-login-activity"
  log_analytics_workspace_id = azurerm_log_analytics_workspace.sentinel_workspace.id
  display_name               = "Suspicious Login Activity"
  severity                   = "High"
  query                      = "SigninLogs | where ResultType != 0"
  trigger_operator           = "GreaterThan"
  trigger_threshold          = 0
  enabled                    = true
}

