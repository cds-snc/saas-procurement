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
