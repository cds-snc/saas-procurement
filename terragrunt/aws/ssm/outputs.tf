output "saas_app_config_arn" {
  description = "Arn of the saas app config parameter"
  value       = aws_ssm_parameter.saas_app_config.arn
}

output "saas_app_config_value" {
  description = "The value of the saas app config parameter"
  value       = aws_ssm_parameter.saas_app_config.value
  sensitive   = true
}

output "approved_request_template_id_arn" {
  description = "Arn of the approved request template id parameter"
  value       = aws_ssm_parameter.approved_request_template_id.arn
}

output "request_s32_approved_template_id_arn" {
  description = "Arn of the request s32 approved template id parameter"
  value       = aws_ssm_parameter.request_s32_approved_template_id.arn
}

output "postgres_password_arn" {
  description = "Arn of the postgress password parameter"
  value       = aws_ssm_parameter.postgres_password.arn
}

output "environment_arn" {
  description = "Arn of the environment parameter"
  value       = aws_ssm_parameter.environment.arn
}

output "sdjango_secret_key_arn" {
  description = "Arn of the django secret key parameter"
  value       = aws_ssm_parameter.django_secret_key.arn
}

output "approver_delete_template_id_arn" {
  description = "Arn of the approver delete template id parameter"
  value       = aws_ssm_parameter.approver_delete_template_id.arn
}

output "social_application_client_id_arn" {
  description = "Arn of the social application client id parameter"
  value       = aws_ssm_parameter.social_application_client_id.arn
}

output "saas_submission_template_id_arn" {
  description = "Arn of the saas submission template id parameter"
  value       = aws_ssm_parameter.saas_submission_template_id.arn
}

output "edit_request_template_id_arn" {
  description = "Arn of the edit request template id parameter"
  value       = aws_ssm_parameter.edit_request_template_id.arn
}

output "delete_saas_request_template_id_arn" {
  description = "Arn of the delete saas request template id parameter"
  value       = aws_ssm_parameter.delete_saas_request_template_id.arn
}

output "saas_submission_edit_template_id_arn" {
  description = "Arn of the saas submission edit template id parameter"
  value       = aws_ssm_parameter.saas_submission_edit_template_id.arn
}

output "denied_request_template_id_arn" {
  description = "Arn of the denied request template id parameter"
  value       = aws_ssm_parameter.denied_request_template_id.arn
}

output "notify_url_arn" {
  description = "Arn of the notify url parameter"
  value       = aws_ssm_parameter.notify_url.arn
}

output "notify_api_key_arn" {
  description = "Arn of the notify api key parameter"
  value       = aws_ssm_parameter.notify_api_key.arn
}

output "approval_request_template_id_arn" {
  description = "Arn of the approval request template id parameter"
  value       = aws_ssm_parameter.approval_request_template_id.arn
}

output "request_s32_denied_internal_ops_template_id_arn" {
  description = "Arn of the request_s32_denied_internal_ops_template_id parameter"
  value       = aws_ssm_parameter.request_s32_denied_internal_ops_template_id.arn
}

output "db_host_arn" {
  description = "Arn of the db host parameter"
  value       = aws_ssm_parameter.db_host.arn
}

output "internal_ops_request_more_info_template_id_arn" {
  description = "Arn of the internal ops request more info template id parameter"
  value       = aws_ssm_parameter.internal_ops_request_more_info_template_id.arn
}

output "postgres_user_arn" {
  description = "Arn of the postgres user parameter"
  value       = aws_ssm_parameter.postgres_user.arn
}

output "request_s32_denied_template_id_arn" {
  description = "Arn of the request s32 denied template id parameter"
  value       = aws_ssm_parameter.request_s32_denied_template_id.arn
}

output "s32_approval_requested_template_id_arn" {
  description = "Arn of the s32 approval requested template id parameter"
  value       = aws_ssm_parameter.s32_approval_requested_template_id.arn
}

output "postgres_db_arn" {
  description = "Arn of the postgres db parameter"
  value       = aws_ssm_parameter.postgres_db.arn
}

output "request_s32_approved_internal_ops_template_id_arn" {
  description = "Arn of the request s32 approved internal ops template id parameter"
  value       = aws_ssm_parameter.request_s32_approved_internal_ops_template_id.arn
}

output "requestor_s32approval_pending_review_template_id_arn" {
  description = "Arn of the requestor s32approval pending review template id parameter"
  value       = aws_ssm_parameter.requestor_s32approval_pending_review_template_id.arn
}

output "social_application_secret_key_arn" {
  description = "Arn of the social application secret key parameter"
  value       = aws_ssm_parameter.social_application_secret_key.arn
}

output "testing_feature_flag_arn" {
  description = "Arn of the testing_feature_flag parameter"
  value       = aws_ssm_parameter.testing_feature_flag.arn
}

output "site_id_arn" {
  description = "Arn of the site id parameter"
  value       = aws_ssm_parameter.site_id.arn
}
