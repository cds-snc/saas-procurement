terraform {
  source = "../../../aws//rds"
}

dependencies {
  paths = ["../network","../ecs"]
}

dependency "network" {
  config_path = "../network"
  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    vpc_id		   = ""
    vpc_private_subnet_ids = [""]
  }
}

dependency "ecs" {
  config_path = "../ecs"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    ecs_tasks_security_group_id = ""
  }
}

inputs = {
  vpc_id	              = dependency.network.outputs.vpc_id
  vpc_private_subnet_ids      = dependency.network.outputs.vpc_private_subnet_ids
  ecs_tasks_security_group_id = dependency.ecs.outputs.ecs_tasks_security_group_id
} 

include {
  path = find_in_parent_folders()
}
