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
  identifier                  = "${var.product_name}_rds"
  instance_class              = "db.t3.micro"
  name                        = "saas_procruement_rds"
  final_snapshot_identifier   = "saas_procurement_rds-${random_string.random.result}"
  username                    = "postgres"
  password                    = aws_ssm_parameter.db_password.value
  backup_retention_period     = 7
  backup_window               = "07:00-09:00"
  allow_major_version_upgrade = true

  # Ignore TFSEC rule as we are using managed KMS
  storage_encrypted = true #tfsec:ignore:AWS051


  vpc_security_group_ids = [
    aws_security_group.saas_procruement_rds.id
  ]

  tags = {
    Name       = "${var.product_name}_database"
    CostCenter = var.product_name
  }
}