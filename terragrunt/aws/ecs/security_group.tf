resource "aws_security_group" "ecs_tasks" {
  name        = "saas-procurement-security-group"
  description = "Allow inbound and outbout traffic for Saas procurement app"
  vpc_id      = var.vpc_id

  ingress {
    protocol        = "tcp"
    security_groups = ["${var.saas_procurement_load_balancer_sg}"]
    self            = "false"
    from_port       = "8000"
    to_port         = "8000"
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "CostCentre" = var.billing_code
  }
}

###
# Traffic to the DB should only come from ECS
#

resource "aws_security_group_rule" "ecs_egress_database" {
  description              = "Allow ECS to talk to the RDS cluster"
  type                     = "egress"
  from_port                = 5432
  to_port                  = 5432
  protocol                 = "TCP"
  source_security_group_id = var.proxy_security_group_id
  security_group_id        = aws_security_group.ecs_tasks.id
}

resource "aws_security_group_rule" "database_ingress_ecs" {
  description              = "Allow RDS cluster to receive requests from ECS"
  type                     = "ingress"
  from_port                = 5432
  to_port                  = 5432
  protocol                 = "TCP"
  source_security_group_id = aws_security_group.ecs_tasks.id 
  security_group_id        = var.proxy_security_group_id
}
