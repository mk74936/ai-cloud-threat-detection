resource "azurerm_resource_group" "rg" {
  name     = "rg-threat-detection"
  location = "East US"
}

resource "azurerm_log_analytics_workspace" "sentinel_workspace" {
  name                = "sentinel-workspace"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "aws_s3_bucket" "security_lake" {
  bucket = "security-lake-bucket-${random_id.bucket_suffix.hex}"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}
