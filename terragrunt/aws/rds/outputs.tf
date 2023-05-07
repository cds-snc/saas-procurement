output "database_proxy_security_group_id" {
  description = "The security group id of the rds cluster"
  value       = module.rds_cluster.proxy_security_group_id
}

output "rds_cluster_id" {
  description = "The id of the rds cluster"
  value       = module.rds_cluster.rds_cluster_id
}

output "proxy_security_group_id" {
  description = "The id of the DB proxy security group"
  value       = module.rds_cluster.proxy_security_group_id
}
