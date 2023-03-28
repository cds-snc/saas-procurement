output "vpc_id" {
  description = "VPC Id"
  value       = module.saas_procurement_vpc.vpc_id
}

output "private_subnet_ids" {
  description = "List of the URL Shortner VPC private subnet ids"
  value       = module.saas_procurement_vpc.private_subnet_ids
}

output "app_security_group_id" {
  description = "App security group Id"
  value       = aws_security_group.app.id
}
