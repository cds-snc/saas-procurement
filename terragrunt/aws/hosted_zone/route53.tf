resource "aws_route53_zone" "saas_procurement" {
  name = var.domain

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}

resource "aws_route53_health_check" "saas_procurement_healthcheck" {
  fqdn              = aws_route53_zone.saas_procurement.name
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health"
  failure_threshold = "3"
  request_interval  = "30"

  tags = {
    "CostCentre" = var.billing_code
  }
}
