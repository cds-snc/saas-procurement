#
# RDS Postgresql database for the Saas procurement app 
#
module "rds_cluster" {
  source = "github.com/cds-snc/terraform-modules?ref=v5.1.4//rds"
  name   = "saas-procurement-database"

  database_name  = var.database_name
  engine         = "aurora-postgresql"
  engine_version = "14.6"
  instances      = var.database_instances_count
  instance_class = "db.r4.large"
  username       = var.database_username
  password       = var.database_password

  backup_retention_period = 14
  preferred_backup_window = "02:00-04:00"

  vpc_id     = var.vpc_id
  subnet_ids = var.private_subnet_ids
  billing_tag_value = var.billing_code
}
