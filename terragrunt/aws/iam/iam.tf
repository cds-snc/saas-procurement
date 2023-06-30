data "aws_iam_policy_document" "saas_procurement" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "saas_procurement_ssm" {

  statement {
    sid    = "AllowSSMAccess"
    effect = "Allow"
    actions = [
      "ssm:GetParametersByPath",
      "ssm:GetParameters",
      "ssm:GetParameter"
    ]
    resources = [
      aws_ssm_parameter.saas_app_config.arn,
      aws_ssm_parameter.approved_request_template_id,
      aws_ssm_parameter.request_s32_approved_template_id,
      aws_ssm_parameter.postgres_password,
      aws_ssm_parameter.environment,
      aws_ssm_parameter.django_secret_key,
      aws_ssm_parameter.approver_delete_template_id,
      aws_ssm_parameter.social_application_client_id,
      aws_ssm_parameter.saas_submission_template_id,
      aws_ssm_parameter.edit_request_template_id,
      aws_ssm_parameter.delete_saas_request_template_id,
      aws_ssm_parameter.saas_submission_edit_template_id,
      aws_ssm_parameter.denied_request_template_id,
      aws_ssm_parameter.notify_url,
      aws_ssm_parameter.notify_api_key,
      aws_ssm_parameter.approval_request_template_id,
      aws_ssm_parameter.request_s32_denied_internal_ops_template_id,
      aws_ssm_parameter.db_host,
      aws_ssm_parameter.internal_ops_request_more_info_template_id,
      aws_ssm_parameter.postgres_user,
      aws_ssm_parameter.request_s32_denied_template_id,
      aws_ssm_parameter.s32_approval_requested_template_id,
      aws_ssm_parameter.postgres_db,
      aws_ssm_parameter.request_s32_approved_internal_ops_template_id,
      aws_ssm_parameter.requestor_s32approval_pending_review_template_id,
      aws_ssm_parameter.social_application_secret_key,
      aws_ssm_parameter.testing_feature_flag,
      aws_ssm_parameter.site_id
    ]
  }
}

resource "aws_iam_policy" "saas_procurement_ssm" {
  name        = "${var.product_name}_Ssm"
  description = "Allow retrieval of ssm data"
  policy      = data.aws_iam_policy_document.saas_procurement_ssm.json

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}

resource "aws_iam_role" "saas_procurement_ecs" {
  name = "saas_procurement-ecs-role"

  assume_role_policy = data.aws_iam_policy_document.saas_procurement.json

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_iam_role" "saas_procurement_task" {
  name = "saas_procurement-task-role"

  assume_role_policy = data.aws_iam_policy_document.saas_procurement.json

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution" {
  role       = aws_iam_role.saas_procurement_ecs.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy_attachment" "saas_procurement_task" {
  role       = aws_iam_role.saas_procurement_task.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy_attachment" "saas_procurement_ssm" {
  policy_arn = aws_iam_policy.saas_procurement_ssm.arn
  role       = aws_iam_role.saas_procurement_task.name
}

