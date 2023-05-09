## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_ecr_repository.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository) | resource |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ecr_repository_arn"></a> [ecr\_repository\_arn](#output\_ecr\_repository\_arn) | Arn of the ECR Repository |
| <a name="output_ecr_repository_url"></a> [ecr\_repository\_url](#output\_ecr\_repository\_url) | URL of the Saas Procurement ECR |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |
| <a name="provider_template"></a> [template](#provider\_template) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_log_group.saas_procurement_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group) | resource |
| [aws_cloudwatch_log_stream.saas_procurement_stream](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_stream) | resource |
| [aws_ecs_cluster.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster) | resource |
| [aws_ecs_service.saas-procurement-app-service](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service) | resource |
| [aws_ecs_task_definition.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition) | resource |
| [aws_security_group.ecs_tasks](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [aws_security_group_rule.database_ingress_ecs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule) | resource |
| [aws_security_group_rule.ecs_egress_database](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule) | resource |
| [template_file.saas_procurement](https://registry.terraform.io/providers/hashicorp/template/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_ecr_repository_arn"></a> [ecr\_repository\_arn](#input\_ecr\_repository\_arn) | Arn of the ECR Repository | `string` | n/a | yes |
| <a name="input_ecr_repository_url"></a> [ecr\_repository\_url](#input\_ecr\_repository\_url) | URL of the Saas Procurement ECR | `string` | n/a | yes |
| <a name="input_ecs_task_policy_attachment"></a> [ecs\_task\_policy\_attachment](#input\_ecs\_task\_policy\_attachment) | ECS Task execution policy attachment | `string` | n/a | yes |
| <a name="input_fargate_cpu"></a> [fargate\_cpu](#input\_fargate\_cpu) | Fargate CPU units | `number` | `512` | no |
| <a name="input_fargate_memory"></a> [fargate\_memory](#input\_fargate\_memory) | Fargate Memory units | `number` | `1024` | no |
| <a name="input_iam_role_saas_procurement_task_arn"></a> [iam\_role\_saas\_procurement\_task\_arn](#input\_iam\_role\_saas\_procurement\_task\_arn) | Arn of the IAM saas procurement task role | `string` | n/a | yes |
| <a name="input_lb_listener"></a> [lb\_listener](#input\_lb\_listener) | Load balancer listener for the Saas procurement app | `string` | n/a | yes |
| <a name="input_lb_target_group_arn"></a> [lb\_target\_group\_arn](#input\_lb\_target\_group\_arn) | Arn of the load balancer target group | `string` | n/a | yes |
| <a name="input_proxy_security_group_id"></a> [proxy\_security\_group\_id](#input\_proxy\_security\_group\_id) | The security group of the RDS proxy | `string` | n/a | yes |
| <a name="input_saas_procurement_load_balancer_sg"></a> [saas\_procurement\_load\_balancer\_sg](#input\_saas\_procurement\_load\_balancer\_sg) | Security group of the Load balancer | `string` | n/a | yes |
| <a name="input_vpc_cidr_block"></a> [vpc\_cidr\_block](#input\_vpc\_cidr\_block) | CIDR block for the Saas Procurement VPC | `list(string)` | <pre>[<br>  "10.0.0.0/16"<br>]</pre> | no |
| <a name="input_vpc_id"></a> [vpc\_id](#input\_vpc\_id) | The VPC id of the url shortener | `string` | n/a | yes |
| <a name="input_vpc_private_subnet_ids"></a> [vpc\_private\_subnet\_ids](#input\_vpc\_private\_subnet\_ids) | Private subnet ids of the Saas Procurement VPC | `list(string)` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ecs_tasks_security_group_id"></a> [ecs\_tasks\_security\_group\_id](#output\_ecs\_tasks\_security\_group\_id) | Id of the ECS tasks security group |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_route53_health_check.saas_procurement_healthcheck](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_health_check) | resource |
| [aws_route53_zone.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_zone) | resource |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_hosted_zone_id"></a> [hosted\_zone\_id](#output\_hosted\_zone\_id) | Route53 hosted zone ID that will hold our DNS records |
| <a name="output_hosted_zone_name"></a> [hosted\_zone\_name](#output\_hosted\_zone\_name) | The name of the route53 hosted zone that will hold our DNS records |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_attach_tf_plan_policy"></a> [attach\_tf\_plan\_policy](#module\_attach\_tf\_plan\_policy) | github.com/cds-snc/terraform-modules | v5.1.4//attach_tf_plan_policy |
| <a name="module_gh_oidc_roles"></a> [gh\_oidc\_roles](#module\_gh\_oidc\_roles) | github.com/cds-snc/terraform-modules | v5.1.4//gh_oidc_role |

## Resources

| Name | Type |
|------|------|
| [aws_iam_policy.saas_procurement_ssm](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy) | resource |
| [aws_iam_role.saas_procurement_ecs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role.saas_procurement_task](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy_attachment.admin](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.ecs_task_execution](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.readonly](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.saas_procurement_ssm](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_role_policy_attachment.saas_procurement_task](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_iam_policy.admin](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy) | data source |
| [aws_iam_policy.readonly](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy) | data source |
| [aws_iam_policy_document.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.saas_procurement_ssm](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_saas_app_config_arn"></a> [saas\_app\_config\_arn](#input\_saas\_app\_config\_arn) | The Arn of saas app config ssm parameter | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ecs_task_policy_attachment"></a> [ecs\_task\_policy\_attachment](#output\_ecs\_task\_policy\_attachment) | ECS Task policy attachment IAM role |
| <a name="output_iam_role_saas_procurement_ecs_arn"></a> [iam\_role\_saas\_procurement\_ecs\_arn](#output\_iam\_role\_saas\_procurement\_ecs\_arn) | Arn of the Saas procurement role |
| <a name="output_iam_role_saas_procurement_task_arn"></a> [iam\_role\_saas\_procurement\_task\_arn](#output\_iam\_role\_saas\_procurement\_task\_arn) | Arn of the Saas procurement task role |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_acm_certificate.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/acm_certificate) | resource |
| [aws_acm_certificate_validation.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/acm_certificate_validation) | resource |
| [aws_lb.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb) | resource |
| [aws_lb_listener.saas_procurement_listener](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_listener) | resource |
| [aws_lb_target_group.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb_target_group) | resource |
| [aws_route53_record.saas_procurement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_record) | resource |
| [aws_route53_record.saas_procurement_certificate_validation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route53_record) | resource |
| [aws_security_group.saas_procurement_load_balancer_sg](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_hosted_zone_id"></a> [hosted\_zone\_id](#input\_hosted\_zone\_id) | The hosted zone ID to create DNS records in | `string` | n/a | yes |
| <a name="input_hosted_zone_name"></a> [hosted\_zone\_name](#input\_hosted\_zone\_name) | Route53 hosted zone ID that will hold our DNS records | `string` | n/a | yes |
| <a name="input_vpc_cidr_block"></a> [vpc\_cidr\_block](#input\_vpc\_cidr\_block) | IP CIDR block of the VPC | `string` | n/a | yes |
| <a name="input_vpc_id"></a> [vpc\_id](#input\_vpc\_id) | The VPC id of the url shortener | `string` | n/a | yes |
| <a name="input_vpc_public_subnet_ids"></a> [vpc\_public\_subnet\_ids](#input\_vpc\_public\_subnet\_ids) | Public subnet ids of the VPC | `list(string)` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_lb_listener"></a> [lb\_listener](#output\_lb\_listener) | Load balancer listener of Saas Procurement |
| <a name="output_lb_target_group_arn"></a> [lb\_target\_group\_arn](#output\_lb\_target\_group\_arn) | Arn of the Load balancer target group |
| <a name="output_saas_procurement_load_balancer_sg"></a> [saas\_procurement\_load\_balancer\_sg](#output\_saas\_procurement\_load\_balancer\_sg) | Security group of the Load balancer |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_saas_procurement_vpc"></a> [saas\_procurement\_vpc](#module\_saas\_procurement\_vpc) | github.com/cds-snc/terraform-modules | v5.1.4//vpc |

## Resources

| Name | Type |
|------|------|
| [aws_security_group.app](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [aws_security_group_rule.app_egress_internet](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule) | resource |

## Inputs

No inputs.

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_app_security_group_id"></a> [app\_security\_group\_id](#output\_app\_security\_group\_id) | App security group Id |
| <a name="output_vpc_cidr_block"></a> [vpc\_cidr\_block](#output\_vpc\_cidr\_block) | List of cidr block ips of the Saas Procurement VPC |
| <a name="output_vpc_id"></a> [vpc\_id](#output\_vpc\_id) | VPC Id |
| <a name="output_vpc_private_subnet_ids"></a> [vpc\_private\_subnet\_ids](#output\_vpc\_private\_subnet\_ids) | List of the Saas Procurement App VPC private subnet ids |
| <a name="output_vpc_public_subnet_ids"></a> [vpc\_public\_subnet\_ids](#output\_vpc\_public\_subnet\_ids) | List of the Saas Procurement App VPC public subnet ids |
## Requirements

No requirements.

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_rds_cluster"></a> [rds\_cluster](#module\_rds\_cluster) | github.com/cds-snc/terraform-modules | v5.1.4//rds |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_database_instances_count"></a> [database\_instances\_count](#input\_database\_instances\_count) | The number of db instances to create | `number` | `1` | no |
| <a name="input_database_name"></a> [database\_name](#input\_database\_name) | The database name of the postgresql database | `string` | n/a | yes |
| <a name="input_database_password"></a> [database\_password](#input\_database\_password) | The password for hte postgresql database | `string` | n/a | yes |
| <a name="input_database_username"></a> [database\_username](#input\_database\_username) | The username of the postgresql database | `string` | n/a | yes |
| <a name="input_vpc_id"></a> [vpc\_id](#input\_vpc\_id) | The VPC id of the url shortener | `string` | n/a | yes |
| <a name="input_vpc_private_subnet_ids"></a> [vpc\_private\_subnet\_ids](#input\_vpc\_private\_subnet\_ids) | The private subnet ids of the VPC | `list(any)` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_database_proxy_security_group_id"></a> [database\_proxy\_security\_group\_id](#output\_database\_proxy\_security\_group\_id) | The security group id of the rds cluster |
| <a name="output_proxy_security_group_id"></a> [proxy\_security\_group\_id](#output\_proxy\_security\_group\_id) | The id of the DB proxy security group |
| <a name="output_rds_cluster_id"></a> [rds\_cluster\_id](#output\_rds\_cluster\_id) | The id of the rds cluster |
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_ssm_parameter.saas_app_config](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ssm_parameter) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_saas_app_config"></a> [saas\_app\_config](#input\_saas\_app\_config) | Environment variables for the Saas Procurement app | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_saas_app_config_arn"></a> [saas\_app\_config\_arn](#output\_saas\_app\_config\_arn) | Arn of the saas app config parameter |
| <a name="output_saas_app_config_value"></a> [saas\_app\_config\_value](#output\_saas\_app\_config\_value) | The value of the saas app config parameter |
