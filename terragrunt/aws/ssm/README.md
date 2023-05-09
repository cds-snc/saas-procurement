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
