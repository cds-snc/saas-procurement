output "hosted_zone_id" {
  description = "Route53 hosted zone ID that will hold our DNS records"
  value       = aws_route53_zone.saas_procurement.zone_id
}

output "hosted_zone_name" {
  description = "The name of the route53 hosted zone that will hold our DNS records"
  value       = aws_route53_zone.saas_procurement.name
}

