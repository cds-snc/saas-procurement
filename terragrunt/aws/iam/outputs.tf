output "iam_role_saas_procurement_arn" {
  description = "ARN of the Saas procurement role"
  value       = aws_iam_role.saas_procurement.arn
}

output "ecs_task_policy_attachment" {
  description = "ECS Task policy attachment IAM role"
  value       = aws_iam_role_policy_attachment.ecs_task_execution
}
