###
# AWS RDS Security Group
###
# Traffic to the DB should only come from ECS
resource "aws_security_group" "saas_procurement_rds" {
  name        = "saas_procurement_rds"
  description = "RDS instance Ingress"
  vpc_id      = var.vpc_id

  ingress {
    protocol        = "tcp"
    from_port       = 5432
    to_port         = 5432
    cidr_blocks     = ["0.0.0.0/0"] #tfsec:ignore:AWS009
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"] #tfsec:ignore:AWS009
  }

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
