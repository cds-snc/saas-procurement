terraform {
  source = "../../../aws//ecs"
}

dependencies {
  paths = ["../ssm", "../iam","../network","../ecr", "../load_balancer", "../rds"]
}

dependency "ssm" {
  config_path = "../ssm"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    saas_app_config_arn = "",
    approved_request_template_id_arn = "",
    request_s32_approved_template_id_arn = "",
    postgres_password_arn = "",
    environment_arn = "",
    django_secret_key_arn = "",
    approver_delete_template_id_arn = "",
    social_application_client_id_arn = "",
    saas_submission_template_id_arn = "",
    edit_request_template_id_arn = "", 
    delete_saas_request_template_id_arn = "",
    saas_submission_edit_template_id = "",
    denied_request_template_id_arn = "",
    notify_url_arn = "",
    notify_api_key_arn = "",
    approval_request_template_id_arn = "",
    request_s32_denied_internal_ops_template_id_arn = "",
    db_host_arn = "",
    internal_ops_request_more_info_template_id_arn = "",
    postgres_user_arn = "",
    request_s32_denied_template_id_arn = "",
    s32_approval_requested_template_id_arn = "",
    postgres_db_arn = "",
    request_s32_approved_internal_ops_template_id_arn = "",
    requestor_s32approval_pending_review_template_id_arn = "",
    saas_submission_edit_template_id_arn = "",
    social_application_secret_key_arn = "",
    testing_feature_flag_arn = "",
    site_id_arn = "", 
  }
}

dependency "iam" {
  config_path = "../iam"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    iam_role_saas_procurement_task_arn = ""
    ecs_task_policy_attachment         = ""
  }
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

dependency "ecr" {
  config_path = "../ecr"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    ecr_repository_arn = ""
    ecr_repository_url = ""
  }
}

dependency "load_balancer" {
  config_path = "../load_balancer"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    lb_listener         	      = ""
    lb_target_group_arn 	      = ""
    saas_procurement_load_balancer_sg = ""
  }
}

dependency "rds" {
  config_path = "../rds"

  mock_outputs_allowed_terraform_commands = ["init", "fmt", "validate", "plan", "show"]
  mock_outputs_merge_with_state           = true
  mock_outputs = {
    proxy_security_group_id = ""
  }
}

inputs = {
  iam_role_saas_procurement_task_arn = dependency.iam.outputs.iam_role_saas_procurement_task_arn
  ecs_task_policy_attachment         = dependency.iam.outputs.ecs_task_policy_attachment
  vpc_private_subnet_ids 	     = dependency.network.outputs.vpc_private_subnet_ids
  vpc_id	         	     = dependency.network.outputs.vpc_id
  ecr_repository_url     	     = dependency.ecr.outputs.ecr_repository_url
  ecr_repository_arn     	     = dependency.ecr.outputs.ecr_repository_arn
  lb_listener            	     = dependency.load_balancer.outputs.lb_listener
  lb_target_group_arn    	     = dependency.load_balancer.outputs.lb_target_group_arn
  saas_procurement_load_balancer_sg  = dependency.load_balancer.outputs.saas_procurement_load_balancer_sg
  proxy_security_group_id	     = dependency.rds.outputs.proxy_security_group_id
  saas_app_config_arn = dependency.ssm.outputs.saas_app_config_arn
  approved_request_template_id_arn = dependency.ssm.outputs.approved_request_template_id_arn 
  request_s32_approved_template_id_arn = dependency.ssm.outputs.request_s32_approved_template_id_arn 
  postgres_password_arn = dependency.ssm.outputs.postgres_password_arn,
  environment_arn = dependency.ssm.outputs.environment_arn,
  django_secret_key_arn = dependency.ssm.outputs.django_secret_key_arn,
  approver_delete_template_id_arn = dependency.ssm.outputs.approver_delete_template_id_arn,
  social_application_client_id_arn = dependency.ssm.outputs.social_application_client_id_arn,
  saas_submission_template_id_arn = dependency.ssm.outputs.saas_submission_template_id_arn,
  edit_request_template_id_arn = dependency.ssm.outputs.edit_request_template_id_arn,
  delete_saas_request_template_id_arn = dependency.ssm.outputs.delete_saas_request_template_id_arn,
  saas_submission_edit_template_id = dependency.ssm.outputs.saas_submission_edit_template_id,
  denied_request_template_id_arn = dependency.ssm.outputs.denied_request_template_id_arn,
  notify_url_arn = dependency.ssm.outputs.notify_url_arn,
  notify_api_key_arn = dependency.ssm.outputs.notify_api_key_arn,
  approval_request_template_id_arn = dependency.ssm.outputs.approval_request_template_id_arn,
  request_s32_denied_internal_ops_template_id_arn = dependency.ssm.outputs.request_s32_denied_internal_ops_template_id_arn,
  db_host_arn = dependency.ssm.outputs.db_host_arn,
  internal_ops_request_more_info_template_id_arn = dependency.ssm.outputs.internal_ops_request_more_info_template_id_arn,
  postgres_user_arn = dependency.ssm.outputs.postgres_user_arn,
  request_s32_denied_template_id_arn = dependency.ssm.outputs.request_s32_denied_template_id_arn,
  s32_approval_requested_template_id_arn = dependency.ssm.outputs.s32_approval_requested_template_id_arn,
  postgres_db_arn = dependency.ssm.outputs.postgres_db_arn,
  request_s32_approved_internal_ops_template_id_arn = dependency.ssm.outputs.request_s32_approved_internal_ops_template_id_arn,
  requestor_s32approval_pending_review_template_id_arn = dependency.ssm.outputs.requestor_s32approval_pending_review_template_id_arn,
  social_application_secret_key_arn = dependency.ssm.outputs.social_application_secret_key_arn,
  testing_feature_flag_arn = dependency.ssm.outputs.testing_feature_flag_arn,
  site_id_arn = dependency.ssm.outputs.site_id_arn,
  saas_submission_edit_template_id_arn = dependency.ssm.outputs.saas_submission_edit_template_id_arn,
} 

include {
  path = find_in_parent_folders()
}
