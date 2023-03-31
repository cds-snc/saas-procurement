output "lb_listener" {
  description = "Load balancer listener of Saas Procurement"
  value       = aws_lb_listener.saas_procurement_listener
}

output "lb_target_group_arn" {
  description = "Arn of the Load balancer target group"
  value       = aws_lb_target_group.saas_procurement.arn
}
