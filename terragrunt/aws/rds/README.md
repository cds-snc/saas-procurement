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
