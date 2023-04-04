
resource "aws_ssm_parameter" "db_password" {
  name  = "/saas_procurement/db_password"
  type  = "SecureString"
  value = var.rds_cluster_password
}
