resource "aws_security_group" "ecs_tasks" {
  name        = "saas-procurement-security-group"
  description = "Allow inbound and outbout traffic for Saas procurement app"
  vpc_id      = var.vpc_id

  ingress {
    protocol    = "tcp"
    from_port   = 8000
    to_port     = 8000
    cidr_blocks = var.vpc_cidr_block
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
