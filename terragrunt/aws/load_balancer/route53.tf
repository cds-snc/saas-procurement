resource "aws_route53_record" "saas_procurement" {
  zone_id = var.hosted_zone_id
  name    = var.hosted_zone_name
  type    = "A"

  alias {
    name                   = aws_lb.saas_procurement.dns_name
    zone_id                = aws_lb.saas_procurement.zone_id
    evaluate_target_health = false
  }
}
