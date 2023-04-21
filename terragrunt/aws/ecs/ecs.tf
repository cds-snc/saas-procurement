# Cluster
resource "aws_ecs_cluster" "saas_procurement" {
  name               = "saas-procurement-cluster"
  capacity_providers = ["FARGATE", "FARGATE_SPOT"]

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
    image                 = "${var.ecr_repository_url}:latest"
    fargate_cpu           = var.fargate_cpu
    fargate_memory        = var.fargate_memory
    aws_region            = "ca-central-1"
  }
}

resource "aws_ecs_task_definition" "saas_procurement" {
  family                   = "saas-procurement-task"
  execution_role_arn       = var.iam_role_saas_procurement_arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  container_definitions    = data.template_file.saas_procurement.rendered
  task_role_arn            = var.iam_role_saas_procurement_task_arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64"
  }
}

# Service
resource "aws_ecs_service" "saas-procurement-app-service" {
  name             = "saas_procurement-service"
  cluster          = aws_ecs_cluster.saas_procurement.id
  task_definition  = aws_ecs_task_definition.saas_procurement.arn
  desired_count    = 2
  launch_type      = "FARGATE"
  platform_version = "1.4.0"
  propagate_tags   = "SERVICE"

  network_configuration {
    security_groups  = [aws_security_group.ecs_tasks.id]
    subnets          = var.vpc_private_subnet_ids
    assign_public_ip = false
  }

  depends_on = [
    var.lb_listener,
    var.ecs_task_policy_attachment
  ]

  load_balancer {
    target_group_arn = var.lb_target_group_arn
    container_name   = "saas-procurement"
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
