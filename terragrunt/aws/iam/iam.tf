data "aws_iam_policy_document" "saas_procurement" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "saas_procurement" {
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
  role       = aws_iam_role.saas_procurement.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
