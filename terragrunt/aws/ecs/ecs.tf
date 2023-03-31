# Cluster
resource "aws_ecs_cluster" "saas_procurement" {
  name = "saas-procurement-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

# Task definition
data "template_file" "saas_procurement" {
  template = file("./templates/saas_procurement.json.tpl")

  vars = {
    awslogs-group         = aws_cloudwatch_log_group.saas_procurement_group.name
    awslogs-region        = "ca-central-1"
    awslogs-stream-prefix = "ecs-saas_procurement"
    image                 = "${aws_ecr_repository.saas_procurement.repository_url}:latest"
    fargate_cpu           = var.fargate_cpu
    fargate_memory        = var.fargate_memory
    aws_region            = "ca-central-1"
  }
}

resource "aws_ecs_task_definition" "saas_procurement" {
  family                   = "saas-procurement-task"
  execution_role_arn       = aws_iam_role.saas_procurement.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  container_definitions    = data.template_file.saas_procurement.rendered
  task_role_arn            = aws_iam_role.saas_procurement.arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64"
  }
}

# Service
resource "aws_ecs_service" "main" {
  name             = "saas_procurement-service"
  cluster          = aws_ecs_cluster.saas_procurement.id
  task_definition  = aws_ecs_task_definition.saas_procurement.arn
  desired_count    = 1
  launch_type      = "FARGATE"
  platform_version = "1.4.0"
  propagate_tags   = "SERVICE"

  network_configuration {
    security_groups  = [aws_security_group.ecs_tasks.id]
    subnets          = module.vpc.private_subnet_ids
    assign_public_ip = false
  }

  depends_on = [
    aws_lb_listener.saas_procurement_listener,
    aws_iam_role_policy_attachment.ecs_task_execution
  ]

  load_balancer {
    target_group_arn = aws_lb_target_group.saas_procurement.arn
    container_name   = "saas_procurement"
    container_port   = 8000
  }

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_cloudwatch_log_group" "saas_procurement_group" {
  name              = "/ecs/saas-procurement-app"
  retention_in_days = 30

  tags = {
    Name = "saas-procurement-log-group"
  }
}

resource "aws_cloudwatch_log_stream" "saas_procurement_stream" {
  name           = "saas-procurement-log-stream"
  log_group_name = aws_cloudwatch_log_group.saas_procurement_group.name
}
