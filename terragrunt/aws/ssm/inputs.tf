# SSM Parameter values
variable "saas_app_config" {
  description = "Environment variables for the Saas Procurement app"
  sensitive   = true
  type        = string
}
