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
      var.saas_app_config_arn,
      var.approved_request_template_id_arn,
      var.request_s32_approved_template_id_arn,
      var.postgres_password_arn,
      var.environment_arn,
      var.django_secret_key_arn,
      var.approver_delete_template_id_arn,
      var.social_application_client_id_arn,
      var.saas_submission_template_id_arn,
      var.edit_request_template_id_arn,
      var.delete_saas_request_template_id_arn,
      var.saas_submission_edit_template_id_arn,
      var.denied_request_template_id_arn,
      var.notify_url_arn,
      var.notify_api_key_arn,
      var.approval_request_template_id_arn,
      var.request_s32_denied_internal_ops_template_id_arn,
      var.db_host_arn,
      var.internal_ops_request_more_info_template_id_arn,
      var.postgres_user_arn,
      var.request_s32_denied_template_id_arn,
      var.s32_approval_requested_template_id_arn,
      var.postgres_db_arn,
      var.request_s32_approved_internal_ops_template_id_arn,
      var.requestor_s32approval_pending_review_template_id_arn,
      var.social_application_secret_key_arn,
      var.testing_feature_flag_arn,
      var.site_id_arn
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

