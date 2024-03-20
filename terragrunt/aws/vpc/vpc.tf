#
# VPC
#

module "vpc" {
  source                            = "github.com/cds-snc/terraform-modules//vpc?ref=v9.2.5"
  name                              = "vpc_name"
  billing_tag_value                 = "saas-procurement" 
  availability_zones                = 3
  single_nat_gateway                = false
  allow_https_requests_in           = true
  allow_https_requests_in_response  = true
  allow_https_requests_out          = true
  allow_https_requests_out_response = true
}

resource "aws_flow_log" "cloud_based_sensor" {
    count                =  1 
    log_destination      = "arn:aws:s3:::cbs-satellite-394954348146/vpc_flow_logs/"
    log_destination_type = "s3"
    traffic_type         = "ALL"
    vpc_id               = module.vpc.vpc_id
    log_format           = "$${vpc-id} $${version} $${account-id} $${interface-id} $${srcaddr} $${dstaddr} $${srcport} $${dstport} $${protocol} $${packets} $${bytes} $${start} $${end} $${action} $${log-status} $${subnet-id} $${instance-id}"
    tags = {
      CostCentre = "saas-procurement"
      Terraform  = true
    }
}