data "aws_iam_policy_document" "saas_procurement" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "saas_procurement_ssm" {

  statement {
    sid    = "AllowSSMAccess"
    effect = "Allow"
    actions = [
      "ssm:GetParametersByPath",
      "ssm:GetParameters",
      "ssm:GetParameter"
    ]
    resources = ["arn:aws:ssm:*:*:parameter/*"]
  }
}

resource "aws_iam_policy" "saas_procurement_ssm" {
  name        = "${var.product_name}_Ssm"
  description = "Allow retrieval of ssm data"
  policy      = data.aws_iam_policy_document.saas_procurement_ssm.json

  tags = {
    CostCentre = var.billing_code
    Terraform  = true
  }
}

resource "aws_iam_role" "saas_procurement_ecs" {
  name = "saas_procurement-ecs-role"

  assume_role_policy = data.aws_iam_policy_document.saas_procurement.json

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_iam_role" "saas_procurement_task" {
  name = "saas_procurement-task-role"

  assume_role_policy = data.aws_iam_policy_document.saas_procurement.json

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution" {
  role       = aws_iam_role.saas_procurement_ecs.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy_attachment" "saas_procurement_task" {
  role       = aws_iam_role.saas_procurement_task.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_iam_role_policy_attachment" "saas_procurement_ssm" {
  policy_arn = aws_iam_policy.saas_procurement_ssm.arn
  role       = aws_iam_role.saas_procurement_task.name
}

