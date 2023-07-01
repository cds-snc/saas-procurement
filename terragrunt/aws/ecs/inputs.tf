variable "vpc_id" {
  description = "The VPC id of the url shortener"
  type        = string
}

variable "vpc_private_subnet_ids" {
  description = "Private subnet ids of the Saas Procurement VPC"
  type        = list(string)
}

variable "vpc_cidr_block" {
  description = "CIDR block for the Saas Procurement VPC"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "ecr_repository_arn" {
  description = "Arn of the ECR Repository"
  type        = string
}

variable "ecr_repository_url" {
  description = "URL of the Saas Procurement ECR"
  type        = string
}

variable "fargate_cpu" {
  description = "Fargate CPU units"
  type        = number
  default     = 512
}

variable "fargate_memory" {
  description = "Fargate Memory units"
  type        = number
  default     = 1024
}

variable "iam_role_saas_procurement_task_arn" {
  description = "Arn of the IAM saas procurement task role"
  type        = string
}

variable "ecs_task_policy_attachment" {
  description = "ECS Task execution policy attachment"
  type        = string
}


variable "lb_listener" {
  description = "Load balancer listener for the Saas procurement app"
  type        = string
}

variable "lb_target_group_arn" {
  description = "Arn of the load balancer target group"
  type        = string
}

variable "saas_procurement_load_balancer_sg" {
  description = "Security group of the Load balancer"
  type        = string
}

variable "proxy_security_group_id" {
  description = "The security group of the RDS proxy"
  type        = string
}

variable "sentinel_customer_id" {
  type      = string
  sensitive = true
}

variable "sentinel_shared_key" {
  type      = string
  sensitive = true
}

variable "saas_app_config_arn" {
  description = "The Arn of saas app config ssm parameter"
  type        = string
}

variable "approved_request_template_id_arn" {
  description = "The approved request notify template id"
  sensitive   = true
  type        = string
}

variable "request_s32_approved_template_id_arn" {
  description = "The request s32 approved notify template id"
  sensitive   = true
  type        = string
}

variable "postgres_password_arn" {
  description = "The password for the postgres user"
  sensitive   = true
  type        = string
}

variable "environment_arn" {
  description = "The environment that we are running (stage, prod or dev)"
  sensitive   = true 
  type        = string
}
variable "django_secret_key_arn" {
  description = "The django secret key"
  sensitive   = true
  type        = string
}

variable "approver_delete_template_id_arn" {
  description = "The approver delete notify template id"
  sensitive   = true
  type        = string
}
variable "social_application_client_id_arn" {
  description = "The social application client id"
  sensitive   = true
  type        = string
}
variable "saas_submission_template_id_arn" {
  description = "The saas submission notify template id"
  sensitive   = true
  type        = string
}
variable "edit_request_template_id_arn" {
  description = "The edit request notify template id"
  sensitive   = true
  type        = string
}
variable "delete_saas_request_template_id_arn" {
  description = "The delete saas request notify template id"
  sensitive   = true
  type        = string
}
variable "saas_submission_edit_template_id_arn" {
  description = "The saas submission edit notify template id"
  sensitive   = true
  type        = string
}
variable "denied_request_template_id_arn" {
  description = "The denied request notify template id"
  sensitive   = true
  type        = string
}
variable "notify_url_arn" {
  description = "The notify url"
  sensitive   = true
  type        = string
}
variable "notify_api_key_arn" {
  description = "The notify api key"
  sensitive   = true
  type        = string
}
variable "approval_request_template_id_arn" {
  description = "The approval request notify template id"
  sensitive   = true
  type        = string
}
variable "request_s32_denied_internal_ops_template_id_arn" {
  description = "The request s32 denied internal ops notify template id"
  sensitive   = true
  type        = string
}
variable "db_host_arn" {
  description = "The database host"
  sensitive   = true
  type        = string
}
variable "internal_ops_request_more_info_template_id_arn" {
  description = "The internal ops request more info notify template id"
  sensitive   = true
  type        = string
}
variable "postgres_user_arn" {
  description = "The postgres user"
  sensitive   = true
  type        = string
}
variable "request_s32_denied_template_id_arn" {
  description = "The request s32 denied notify template id"
  sensitive   = true
  type        = string
}
variable "s32_approval_requested_template_id_arn" {
  description = "The s32 approval requested notify template id"
  sensitive   = true
  type        = string
}
variable "postgres_db_arn" {
  description = "The postgres database"
  sensitive   = true
  type        = string
}
variable "request_s32_approved_internal_ops_template_id_arn" {
  description = "The request s32 approved internal ops notify template id"
  sensitive   = true
  type        = string
}
variable "requestor_s32approval_pending_review_template_id_arn" {
  description = "The requestor s32approval pending review notify template id"
  sensitive   = true
  type        = string
}
variable "social_application_secret_key_arn" {
  description = "The social application secret key"
  sensitive   = true
  type        = string
}
variable "testing_feature_flag_arn" {
  description = "The testing feature flag"
  sensitive   = true 
  type        = string
}
variable "site_id_arn" {
  description = "The site id for the social application"
  sensitive   = true 
  type        = string
}
