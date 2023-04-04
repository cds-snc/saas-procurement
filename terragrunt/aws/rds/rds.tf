resource "random_string" "random" {
  length  = 6
  special = false
  upper   = false
}

resource "aws_db_instance" "saas_procurement_database" {
  allocated_storage           = 20
  storage_type                = "gp2"
  engine                      = "postgres"
  engine_version              = "14.4"
  identifier                  = "saas-procurement-rds"
  instance_class              = "db.t3.micro"
  final_snapshot_identifier   = "saas_procurement_rds-${random_string.random.result}"
  iam_database_authentication_enabled = true
  username                    = "postgres"
  password                    = aws_ssm_parameter.db_password.value
  backup_retention_period     = 7
  backup_window               = "07:00-09:00"
  monitoring_interval  	      = 5
  multi_az                    = true 
  enabled_cloudwatch_logs_exports = ["general", "error", "slowquery"]
  allow_major_version_upgrade = true
  auto_minor_version_upgrade = true
  storage_encrypted = true 

  vpc_security_group_ids = [
    aws_security_group.saas_procurement_rds.id
  ]

  tags = {
    Name       = "${var.product_name}-database"
    CostCenter = var.product_name
  }
}
