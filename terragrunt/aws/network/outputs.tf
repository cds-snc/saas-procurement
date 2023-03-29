output "vpc_id" {
  description = "VPC Id"
  value       = module.saas_procurement_vpc.vpc_id
}

output "vpc_private_subnet_ids" {
  description = "List of the Saas Procurement App VPC private subnet ids"
  value       = module.saas_procurement_vpc.private_subnet_ids
}

output "vpc_public_subnet_ids" {
  description = "List of the Saas Procurement App VPC public subnet ids"
  value       = module.saas_procurement_vpc.public_subnet_ids
}

output "vpc_cidr_block" {
  description = "List of cidr block ips of the Saas Procurement VPC"
  value       = module.saas_procurement_vpc.cidr_block
}


output "app_security_group_id" {
  description = "App security group Id"
  value       = aws_security_group.app.id
}
