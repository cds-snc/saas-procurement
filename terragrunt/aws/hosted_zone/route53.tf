resource "aws_route53_zone" "saas_procurement" {
  name = var.domain

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
