
# RDS Postgresql database for the Saas procurement app 
#
module "rds_cluster" {
  source = "github.com/cds-snc/terraform-modules?ref=v5.1.4//rds"
  name   = "saas-procurement-database"

  database_name  = var.postgres_db
  engine         = "aurora-postgresql"
  engine_version = "14.6"
  instances      = var.database_instances_count
  instance_class = "db.serverless"
  username       = var.postgres_user
  password       = var.postgres_password

  serverless_min_capacity = 1.0
  serverless_max_capacity = 2.0

  backup_retention_period = 14
  preferred_backup_window = "02:00-04:00"

  vpc_id            = var.vpc_id
  subnet_ids        = var.vpc_private_subnet_ids
  billing_tag_value = var.billing_code
}
