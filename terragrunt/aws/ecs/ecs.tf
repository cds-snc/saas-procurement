module "saas_procurement" {
  source = "github.com/cds-snc/terraform-modules//ecs?ref=v7.2.7"

  # Cluster and service
  cluster_name = "saas-procurement-cluster"
  service_name = "saas-procurement-app-service"
  depends_on = [
    var.lb_listener,
    var.ecs_task_policy_attachment
  ]

  # Task/Container definition
  container_image     = "${var.ecr_repository_url}:latest"
  container_name      = "saas-procurement"
  task_cpu            = var.fargate_cpu
  task_memory         = var.fargate_memory
  container_port      = 8000
  container_host_port = 8000

  # Task definition
  task_name          = "saas-procurement-task"
  task_exec_role_arn = var.iam_role_saas_procurement_task_arn
  task_role_arn      = var.iam_role_saas_procurement_task_arn


  # Scaling
  enable_autoscaling = true

  # Networking
  lb_target_group_arn = var.lb_target_group_arn
  security_group_ids  = [aws_security_group.ecs_tasks.id]
  subnet_ids          = var.vpc_private_subnet_ids

  billing_tag_value = var.billing_code
}


resource "aws_cloudwatch_log_stream" "saas_procurement_stream" {
  name           = "saas-procurement-log-stream"
  log_group_name = "/aws/ecs/saas-procurement-cluster"
}