resource "aws_security_group" "saas_procurement_load_balancer" {
  name        = "Saas Procurement load balancer"
  description = "Ingress of Saas Procurement Load Balancer"
  vpc_id      = var.vpc_id

  ingress {
    protocol    = "tcp"
    from_port   = 443
    to_port     = 443
    cidr_blocks = ["0.0.0.0/0"] #tfsec:ignore:AWS008
  }

  egress {
    protocol    = "tcp"
    from_port   = 8000
    to_port     = 8000
    cidr_blocks = [var.vpc_cidr_block] #tfsec:ignore:AWS008
  }

  tags = {
    "CostCentre" = var.billing_code
  }
}
