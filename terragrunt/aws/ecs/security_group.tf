resource "aws_security_group" "ecs_tasks" {
  name        = "saas-procurement-security-group"
  description = "Allow inbound and outbout traffic for Saas procurement app"
  vpc_id      = var.vpc_id

  ingress {
    from_port       = "0"
    protocol        = "tcp"
    security_groups = [var.saas_procurement_load_balancer_sg]
    self            = "false"
    to_port         = "65535"
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
