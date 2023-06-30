resource "aws_ssm_parameter" "saas_app_config" {
  name  = "saas_app_config"
  type  = "SecureString"
  value = var.saas_app_config

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}

resource "aws_ssm_parameter" "approved_request_template_id" {
  name  = "approved_request_template_id"
  type  = "SecureString"
  value = var.approved_request_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}

resource "aws_ssm_parameter" "request_s32_approved_template_id" {
  name  = "request_s32_approved_template_id"
  type  = "String"
  value = var.request_s32_approved_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "postgres_password" {
  name  = "postgres_password"
  type  = "SecureString"
  value = var.postgres_password

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "environment" {
  name  = "environment"
  type  = "SecureString"
  value = var.environment

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "django_secret_key" {
  name  = "django_secret_key"
  type  = "SecureString"
  value = var.django_secret_key

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "approver_delete_template_id" {
  name  = "approver_delete_template_id"
  type  = "SecureString"
  value = var.approver_delete_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "social_application_client_id" {
  name  = "social_application_client_id"
  type  = "SecureString"
  value = var.social_application_client_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "saas_submission_template_id" {
  name  = "saas_submission_template_id"
  type  = "SecureString"
  value = var.saas_submission_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "edit_request_template_id" {
  name  = "edit_request_template_id"
  type  = "SecureString"
  value = var.edit_request_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "delete_saas_request_template_id" {
  name  = "delete_saas_request_template_id"
  type  = "SecureString"
  value = var.delete_saas_request_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "saas_submission_edit_template_id" {
  name  = "saas_submission_edit_template_id"
  type  = "SecureString"
  value = var.saas_submission_edit_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "denied_request_template_id" {
  name  = "denied_request_template_id"
  type  = "SecureString"
  value = var.denied_request_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "notify_url" {
  name  = "notify_url"
  type  = "SecureString"
  value = var.notify_url

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "notify_api_key" {
  name  = "notify_api_key"
  type  = "SecureString"
  value = var.notify_api_key

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "approval_request_template_id" {
  name  = "approval_request_template_id"
  type  = "SecureString"
  value = var.approval_request_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "request_s32_denied_internal_ops_template_id" {
  name  = "request_s32_denied_internal_ops_template_id"
  type  = "SecureString"
  value = var.request_s32_denied_internal_ops_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "db_host" {
  name  = "db_host"
  type  = "SecureString"
  value = var.db_host

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "internal_ops_request_more_info_template_id" {
  name  = "internal_ops_request_more_info_template_id"
  type  = "SecureString"
  value = var.internal_ops_request_more_info_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "postgres_user" {
  name  = "postgres_user"
  type  = "SecureString"
  value = var.postgres_user

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "request_s32_denied_template_id" {
  name  = "request_s32_denied_template_id"
  type  = "SecureString"
  value = var.request_s32_denied_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "s32_approval_requested_template_id" {
  name  = "s32_approval_requested_template_id"
  type  = "SecureString"
  value = var.s32_approval_requested_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "postgres_db" {
  name  = "postgres_db"
  type  = "SecureString"
  value = var.postgres_db

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "request_s32_approved_internal_ops_template_id" {
  name  = "request_s32_approved_internal_ops_template_id"
  type  = "SecureString"
  value = var.request_s32_approved_internal_ops_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "requestor_s32approval_pending_review_template_id" {
  name  = "requestor_s32approval_pending_review_template_id"
  type  = "SecureString"
  value = var.requestor_s32approval_pending_review_template_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "social_application_secret_key" {
  name  = "social_application_secret_key"
  type  = "SecureString"
  value = var.social_application_secret_key

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "testing_feature_flag" {
  name  = "testing_feature_flag"
  type  = "SecureString"
  value = var.testing_feature_flag

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
resource "aws_ssm_parameter" "site_id" {
  name  = "site_id"
  type  = "SecureString"
  value = var.site_id

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}
