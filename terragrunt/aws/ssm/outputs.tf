output "postgres_password_arn" {
  description = "Arn of the postgres db password"
  value       = aws_ssm_parameter.db_password.arn
}

output "postgres_password_value" {
  description = "The value of the postgres db password"
  value       = aws_ssm_parameter.db_password.value
  sensitive   = true
}
