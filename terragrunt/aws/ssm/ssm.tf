resource "aws_ssm_parameter" "saas_app_config" {
  name  = "saas_app_config"
  type  = "SecureString"
  value = var.saas_app_config

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
