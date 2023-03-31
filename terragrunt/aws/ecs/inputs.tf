variable "vpc_id" {
  description = "The VPC id of the url shortener"
  type        = string
}

variable "vpc_private_subnet_ids" {
  description = "Private subnet ids of the Saas Procurement VPC"
  type	      = list(string)
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
  default     = 256
}

variable "fargate_memory" {
  description = "Fargate Memory units"
  type        = number
  default     = 512
}

variable "iam_role_saas_procurement_arn" {
  description = "Arn of the IAM saas procurement role"
  type 	      = string
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
