terraform {
  source = "../../../aws//iam"
}

include {
  path = find_in_parent_folders()
}
