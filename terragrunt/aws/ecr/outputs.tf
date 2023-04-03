output "ecr_repository_url" {
  description = "URL of the Saas Procurement ECR"
  value       = aws_ecr_repository.saas_procurement.repository_url
}

output "ecr_repository_arn" {
  description = "Arn of the ECR Repository"
  value       = aws_ecr_repository.saas_procurement.arn
}
