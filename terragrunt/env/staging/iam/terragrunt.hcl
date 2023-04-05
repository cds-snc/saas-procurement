terraform {
  source = "../../../aws//iam"
}

dependencies {
  paths = ["../ssm"]
}

dependency "ssm" {
  config_path = "../ssm"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    postgres_password_arn = ""
  }
}

inputs = {
  postgres_password_arn  = dependency.ssm.outputs.postgres_password_arn
}

include {
  path = find_in_parent_folders()
}
