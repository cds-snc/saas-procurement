resource "aws_ecr_repository" "saas_procurement" {
  name                 = "saas-procurement"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
