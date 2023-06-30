# SSM Parameter values
variable "saas_app_config" {
  description = "Environment variables for the Saas Procurement app"
  sensitive   = true
  type        = string
}

variable "approved_request_template_id" {
  description = "The approved request notify template id"
  sensitive   = true
  type        = string
}

variable "request_s32_approved_template_id" {
  description = "The request s32 approved notify template id"
  sensitive   = true
  type        = string
}

variable "postgres_password" {
  description = "The password for the postgres user"
  sensitive   = true
  type        = string
}

variable "environment" {
  description = "The environment that we are running (stage, prod or dev)"
  sensitive   = true 
  type        = string
}
variable "django_secret_key" {
  description = "The django secret key"
  sensitive   = true
  type        = string
}

variable "approver_delete_template_id" {
  description = "The approver delete notify template id"
  sensitive   = true
  type        = string
}
variable "social_application_client_id" {
  description = "The social application client id"
  sensitive   = true
  type        = string
}
variable "saas_submission_template_id" {
  description = "The saas submission notify template id"
  sensitive   = true
  type        = string
}
variable "edit_request_template_id" {
  description = "The edit request notify template id"
  sensitive   = true
  type        = string
}
variable "delete_saas_request_template_id" {
  description = "The delete saas request notify template id"
  sensitive   = true
  type        = string
}
variable "saas_submission_edit_template_id" {
  description = "The saas submission edit notify template id"
  sensitive   = true
  type        = string
}
variable "denied_request_template_id" {
  description = "The denied request notify template id"
  sensitive   = true
  type        = string
}
variable "notify_url" {
  description = "The notify url"
  sensitive   = true
  type        = string
}
variable "notify_api_key" {
  description = "The notify api key"
  sensitive   = true
  type        = string
}
variable "approval_request_template_id" {
  description = "The approval request notify template id"
  sensitive   = true
  type        = string
}
variable "request_s32_denied_internal_ops_template_id" {
  description = "The request s32 denied internal ops notify template id"
  sensitive   = true
  type        = string
}
variable "db_host" {
  description = "The database host"
  sensitive   = true
  type        = string
}
variable "internal_ops_request_more_info_template_id" {
  description = "The internal ops request more info notify template id"
  sensitive   = true
  type        = string
}
variable "postgres_user" {
  description = "The postgres user"
  sensitive   = true
  type        = string
}
variable "request_s32_denied_template_id" {
  description = "The request s32 denied notify template id"
  sensitive   = true
  type        = string
}
variable "s32_approval_requested_template_id" {
  description = "The s32 approval requested notify template id"
  sensitive   = true
  type        = string
}
variable "postgres_db" {
  description = "The postgres database"
  sensitive   = true
  type        = string
}
variable "request_s32_approved_internal_ops_template_id" {
  description = "The request s32 approved internal ops notify template id"
  sensitive   = true
  type        = string
}
variable "requestor_s32approval_pending_review_template_id" {
  description = "The requestor s32approval pending review notify template id"
  sensitive   = true
  type        = string
}
variable "social_application_secret_key" {
  description = "The social application secret key"
  sensitive   = true
  type        = string
}
variable "testing_feature_flag" {
  description = "The testing feature flag"
  sensitive   = true 
  type        = string
}
variable "site_id" {
  description = "The site id for the social application"
  sensitive   = true 
  type        = string
}