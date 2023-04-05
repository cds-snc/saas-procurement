# RDS database password
variable "postgres_password_value" {
  description = "RDS password"
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
