locals {
  oidc_role = "OIDCGithubWorkflowRole"
}

data "aws_caller_identity" "current" {}

module "gh_oidc_roles" {
  source = "github.com/cds-snc/terraform-modules?ref=v3.0.17//gh_oidc_role"
  roles = [
    {
      name      = local.oidc_role
      repo_name = "saas-procurement"
      claim     = "*"
    }
  ]

  billing_tag_value = var.billing_code
}

module "attach_tf_plan_policy" {
  source            = "github.com/cds-snc/terraform-modules?ref=v5.1.4//attach_tf_plan_policy"
  account_id        = data.aws_caller_identity.current.account_id
  role_name         = local.oidc_role
  bucket_name       = "${var.billing_code}-tf"
  lock_table_name   = "terraform-state-lock-dynamo"
  billing_tag_value = var.billing_code
  depends_on = [
    module.gh_oidc_roles
  ]
}

data "aws_iam_policy" "admin" {
  name = "AdministratorAccess"
  depends_on = [
    module.gh_oidc_roles
  ]
}

resource "aws_iam_role_policy_attachment" "admin" {
  role       = local.oidc_role
  policy_arn = data.aws_iam_policy.admin.arn
  depends_on = [
    module.gh_oidc_roles
  ]
}
