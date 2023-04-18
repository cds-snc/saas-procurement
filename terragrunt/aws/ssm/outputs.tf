output "saas_app_config_arn" {
  description = "Arn of the saas app config parameter"
  value       = aws_ssm_parameter.saas_app_config.arn
}

output "saas_app_config_value" {
  description = "The value of the saas app config parameter"
  value       = aws_ssm_parameter.saas_app_config.value
  sensitive   = true
}
