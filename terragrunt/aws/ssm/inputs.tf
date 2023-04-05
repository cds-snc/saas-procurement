# RDS database password
variable "postgres_password" {
  description = "RDS password"
  sensitive   = true
  type        = string
}
