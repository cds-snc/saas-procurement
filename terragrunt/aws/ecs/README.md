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
