# 
# Security Groups for the VPC Saas Procurement app 
#

resource "aws_security_group" "app" {

  name        = "${var.product_name}_app_sg"
  description = "SG for the Saas Procurement App"

  vpc_id = module.saas_procurement_vpc.vpc_id

  tags = {
    CostCentre = var.billing_code
    Name       = "${var.product_name}_app_sg"
  }
}

resource "aws_security_group_rule" "app_egress_internet" {
  description       = "Allow TCP egress connections to the internet on port 443"
  type              = "egress"
  from_port         = 443
  to_port           = 443
  protocol          = "TCP"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.app.id
}
