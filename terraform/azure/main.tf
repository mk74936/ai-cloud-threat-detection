provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "sentinel_rg" {
  name     = "sentinel-lab-rg"
  location = "East US"
}

resource "azurerm_log_analytics_workspace" "law" {
  name                = "sentinel-lab-workspace"
  location            = azurerm_resource_group.sentinel_rg.location
  resource_group_name = azurerm_resource_group.sentinel_rg.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

resource "azurerm_sentinel_alert_rule_scheduled" "example" {
  name                       = "failed-login-alert"
  log_analytics_workspace_id = azurerm_log_analytics_workspace.law.id
  display_name               = "Failed Logins Alert"
  description                = "Detects EventID 4625 failures"
  severity                   = "Medium"
  enabled                    = true
  query                      = "SecurityEvent | where EventID == 4625"
  query_frequency            = "PT1H"
  query_period               = "PT1H"
  trigger_operator           = "GreaterThan"
  trigger_threshold          = 0
  tactics                    = ["InitialAccess"]
}
