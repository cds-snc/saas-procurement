# RDS database password
variable "rds_cluster_password" {
  description = "RDS cluster password"
  sensitive   = true
  type        = string
}

variable "vpc_id" {
  description = "The VPC id of the url shortener"
  type        = string
}

variable "ecs_tasks_security_group_id" {
  description = "Id of the ECS tasks security group"
  type        = string
}
