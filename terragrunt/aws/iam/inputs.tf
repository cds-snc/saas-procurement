variable "saas_app_config_arn" {
  description = "The Arn of saas app config ssm parameter"
  type        = string
}

variable "approved_request_template_id_arn" {
  description = "The approved request notify template id"
  type        = string
}

variable "request_s32_approved_template_id_arn" {
  description = "The request s32 approved notify template id"
  type        = string
}

variable "postgres_password_arn" {
  description = "The password for the postgres user"
  type        = string
}

variable "environment_arn" {
  description = "The environment that we are running (stage, prod or dev)"
  type        = string
}
variable "django_secret_key_arn" {
  description = "The django secret key"
  type        = string
}

variable "approver_delete_template_id_arn" {
  description = "The approver delete notify template id"
  type        = string
}
variable "social_application_client_id_arn" {
  description = "The social application client id"
  type        = string
}
variable "saas_submission_template_id_arn" {
  description = "The saas submission notify template id"
  type        = string
}
variable "edit_request_template_id_arn" {
  description = "The edit request notify template id"
  type        = string
}
variable "delete_saas_request_template_id_arn" {
  description = "The delete saas request notify template id"
  type        = string
}
variable "saas_submission_edit_template_id_arn" {
  description = "The saas submission edit notify template id"
  type        = string
}
variable "denied_request_template_id_arn" {
  description = "The denied request notify template id"
  type        = string
}
variable "notify_url_arn" {
  description = "The notify url"
  type        = string
}
variable "notify_api_key_arn" {
  description = "The notify api key"
  type        = string
}
variable "approval_request_template_id_arn" {
  description = "The approval request notify template id"
  type        = string
}
variable "request_s32_denied_internal_ops_template_id_arn" {
  description = "The request s32 denied internal ops notify template id"
  type        = string
}
variable "db_host_arn" {
  description = "The database host"
  type        = string
}
variable "internal_ops_request_more_info_template_id_arn" {
  description = "The internal ops request more info notify template id"
  type        = string
}
variable "postgres_user_arn" {
  description = "The postgres user"
  type        = string
}
variable "request_s32_denied_template_id_arn" {
  description = "The request s32 denied notify template id"
  type        = string
}
variable "s32_approval_requested_template_id_arn" {
  description = "The s32 approval requested notify template id"
  type        = string
}
variable "postgres_db_arn" {
  description = "The postgres database"
  type        = string
}
variable "request_s32_approved_internal_ops_template_id_arn" {
  description = "The request s32 approved internal ops notify template id"
  type        = string
}
variable "requestor_s32approval_pending_review_template_id_arn" {
  description = "The requestor s32approval pending review notify template id"
  type        = string
}
variable "social_application_secret_key_arn" {
  description = "The social application secret key"
  type        = string
}
variable "testing_feature_flag_arn" {
  description = "The testing feature flag"
  type        = string
}
variable "site_id_arn" {
  description = "The site id for the social application"
  type        = string
}
