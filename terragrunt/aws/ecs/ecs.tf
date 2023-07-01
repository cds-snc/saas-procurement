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
    image                 = "${var.ecr_repository_url}:latest"
    fargate_cpu           = var.fargate_cpu
    fargate_memory        = var.fargate_memory
    aws_region            = "ca-central-1"

    APPROVED_REQUEST_TEMPLATE_ID                     = var.approved_request_template_id_arn
    REQUEST_S32_APPROVED_TEMPLATE_ID                 = var.request_s32_approved_template_id_arn
    POSTGRES_PASSWORD                                = var.postgres_password_arn
    ENVIRONMENT                                      = var.environment_arn
    DJANGO_SECRET_KEY                                = var.django_secret_key_arn
    APPROVER_DELETE_TEMPLATE_ID                      = var.approver_delete_template_id_arn
    SOCIAL_APPLICATION_CLIENT_ID                     = var.social_application_client_id_arn
    SAAS_SUBMISSION_TEMPLATE_ID                      = var.saas_submission_template_id_arn
    EDIT_REQUEST_TEMPLATE_ID                         = var.edit_request_template_id_arn
    DELETE_SAAS_REQUEST_TEMPLATE_ID                  = var.delete_saas_request_template_id_arn
    SAAS_SUBMISSION_EDIT_TEMPLATE_ID                 = var.saas_submission_edit_template_id_arn
    DENIED_REQUEST_TEMPLATE_ID                       = var.denied_request_template_id_arn
    NOTIFY_URL                                       = var.notify_url_arn
    NOTIFY_API_KEY                                   = var.notify_api_key_arn
    APPROVAL_REQUEST_TEMPLATE_ID                     = var.approval_request_template_id_arn
    REQUEST_S32_DENIED_INTERNAL_OPS_TEMPLATE_ID      = var.request_s32_denied_internal_ops_template_id_arn
    DB_HOST                                          = var.db_host_arn
    INTERNAL_OPS_REQUEST_MORE_INFO_TEMPLATE_ID       = var.internal_ops_request_more_info_template_id_arn
    POSTGRES_USER                                    = var.postgres_user_arn
    REQUEST_S32_DENIED_TEMPLATE_ID                   = var.request_s32_denied_template_id_arn
    S32_APPROVAL_REQUESTED_TEMPLATE_ID               = var.s32_approval_requested_template_id_arn
    POSTGRES_DB                                      = var.postgres_db_arn
    REQUEST_S32_APPROVED_INTERNAL_OPS_TEMPLATE_ID    = var.request_s32_approved_internal_ops_template_id_arn
    REQUESTOR_S32APPROVAL_PENDING_REVIEW_TEMPLATE_ID = var.requestor_s32approval_pending_review_template_id_arn
    SOCIAL_APPLICATION_SECRET_KEY                    = var.social_application_secret_key_arn
    TESTING_FEATURE_FLAG                             = var.testing_feature_flag_arn
    SITE_ID                                          = var.site_id_arn
  }
}

resource "aws_ecs_task_definition" "saas_procurement" {
  family                   = "saas-procurement-task"
  execution_role_arn       = var.iam_role_saas_procurement_task_arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  container_definitions    = data.template_file.saas_procurement.rendered
  task_role_arn            = var.iam_role_saas_procurement_task_arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
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

module "sentinel_forwarder" {
  source            = "github.com/cds-snc/terraform-modules?ref=v6.1.0//sentinel_forwarder"
  function_name     = "sentinel-forwarder"
  billing_tag_value = var.billing_tag_value

  layer_arn = "arn:aws:lambda:ca-central-1:283582579564:layer:aws-sentinel-connector-layer:71"

  customer_id = var.sentinel_customer_id
  shared_key  = var.sentinel_shared_key

  cloudwatch_log_arns = [aws_cloudwatch_log_group.saas_procurement_group.arn]
}

resource "aws_cloudwatch_log_subscription_filter" "sentinel_forwarder" {
  name            = "All ECS logs"
  log_group_name  = aws_cloudwatch_log_group.saas_procurement_group.name
  filter_pattern  = "[w1=\"*\"]"
  destination_arn = module.sentinel_forwarder.lambda_arn
  distribution    = "Random"
}
