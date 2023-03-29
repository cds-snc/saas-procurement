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

resource "aws_security_group" "vpc_endpoint" {
  name        = "vpc_endpoints"
  description = "PrivateLink VPC endpoints"
  vpc_id      = module.saas_procurement_vpc.vpc_id

  tags = {
    Name       = "${var.product_name}_app_sg"
    CostCentre = var.billing_code
    Terraform  = true
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

resource "aws_security_group_rule" "vpc_endpoint_interface_ingress" {
  description              = "Ingress from the App security group to the private interface endpoints"
  type                     = "ingress"
  from_port                = 443
  to_port                  = 443
  protocol                 = "tcp"
  security_group_id        = aws_security_group.vpc_endpoint.id
  source_security_group_id = aws_security_group.app.id
}

resource "aws_security_group_rule" "s3_private_endpoint_ingress" {
  description       = "Ingress from the private S3 endpoint"
  type              = "ingress"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  security_group_id = aws_security_group.vpc_endpoint.id
  prefix_list_ids = [
    aws_vpc_endpoint.s3.prefix_list_id
  ]
}
