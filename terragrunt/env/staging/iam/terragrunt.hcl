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
    saas_app_config_arn = "",
    approved_request_template_id = "",
    request_s32_approved_template_id = "",
    postgres_password = "",
    environment = "",
    django_secret_key = "",
    approver_delete_template_id = "",
    social_application_client_id = "",
    saas_submission_template_id = "",
    edit_request_template_id = "", 
    delete_saas_request_template_id = "",
    saas_submission_edit_template_id = "",
    denied_request_template_id = "",
    notify_url = "",
    notify_api_key = "",
    approval_request_template_id = "",
    request_s32_denied_internal_ops_template_id = "",
    db_host = "",
    internal_ops_request_more_info_template_id = "",
    postgres_user = "",
    request_s32_denied_template_id = "",
    s32_approval_requested_template_id = "",
    postgres_db = "",
    request_s32_approved_internal_ops_template_id = "",
    requestor_s32approval_pending_review_template_id = "",
    social_application_secret_key = "",
    testing_feature_flag = "",
    site_id = "", 
  }
}

inputs = {
  saas_app_config_arn = dependency.ssm.outputs.saas_app_config_arn
}

include {
  path = find_in_parent_folders()
}
