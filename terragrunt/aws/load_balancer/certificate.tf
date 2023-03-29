resource "aws_acm_certificate" "saas_procurement" {
  domain_name               = "saas.cdssandbox.xyz"
  subject_alternative_names = ["*.saas.cdssandbox.xyz"]
  validation_method         = "DNS"

  tags = {
    "CostCentre" = var.billing_code
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_route53_record" "saas_procurement_certificate_validation" {
  zone_id = var.hosted_zone_id

  for_each = {
    for dvo in aws_acm_certificate.saas_procurement.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      type   = dvo.resource_record_type
      record = dvo.resource_record_value
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  type            = each.value.type

  ttl = 60
}

resource "aws_acm_certificate_validation" "saas_procurement" {
  certificate_arn         = aws_acm_certificate.saas_procurement.arn
  validation_record_fqdns = [for record in aws_route53_record.saas_procurement_certificate_validation : record.fqdn]
}
