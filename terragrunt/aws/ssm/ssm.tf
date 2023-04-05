
resource "aws_ssm_parameter" "db_password" {
  name  = "/saas_procurement/db_password"
  type  = "SecureString"
  value = "POSTGRES_PASSWORD=${var.postgres_password}"

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
