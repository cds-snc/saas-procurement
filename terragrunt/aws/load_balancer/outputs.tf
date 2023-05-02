output "lb_listener" {
  description = "Load balancer listener of Saas Procurement"
  value       = aws_lb_listener.saas_procurement_listener
}

output "lb_target_group_arn" {
  description = "Arn of the Load balancer target group"
  value       = aws_lb_target_group.saas_procurement.arn
}

output "saas_procurement_load_balancer_sg" {
  description = "Security group of the Load balancer"
  value       = aws_security_group.saas_procurement_load_balancer_sg.id
}
