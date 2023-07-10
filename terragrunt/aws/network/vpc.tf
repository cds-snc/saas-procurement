#
# VPC
#

module "saas_procurement_vpc" {
  source            = "github.com/cds-snc/terraform-modules?//vpc?ref=v6.1.1"
  name              = var.product_name
  billing_tag_value = var.billing_code
  high_availability = true
  enable_flow_log   = true
  block_ssh         = true
  block_rdp         = true

  single_nat_gateway = var.env != "production"

  allow_https_request_out          = true
  allow_https_request_out_response = true
  allow_https_request_in           = true
  allow_https_request_in_response  = true
}
