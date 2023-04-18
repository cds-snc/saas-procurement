resource "aws_lb" "saas_procurement" {

  name               = "saas-procurement-alb"
  internal           = false #tfsec:ignore:AWS005
  load_balancer_type = "application"

  enable_deletion_protection = true
  drop_invalid_header_fields = true

  security_groups = [
    aws_security_group.saas_procurement_load_balancer_sg.id
  ]

  subnets = var.vpc_public_subnet_ids

  tags = {
    "CostCentre" = var.billing_code
  }
}

resource "aws_lb_listener" "saas_procurement_listener" {
  depends_on = [
    aws_acm_certificate.saas_procurement,
    aws_route53_record.saas_procurement_certificate_validation,
    aws_acm_certificate_validation.saas_procurement,
  ]

  load_balancer_arn = aws_lb.saas_procurement.arn
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "EELBSecurityPolicy-TLS13-1-2-2021-06"
  certificate_arn   = aws_acm_certificate.saas_procurement.arn

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.saas_procurement.arn
  }
}

resource "aws_lb_target_group" "saas_procurement" {
  name                 = "saas-procurement"
  port                 = 8000
  protocol             = "HTTP"
  protocol_version     = "HTTP1"
  target_type          = "ip"
  deregistration_delay = 30
  vpc_id               = var.vpc_id

  health_check {
    enabled             = true
    interval            = 10
    path                = "/health"
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }

  tags = {
    "CostCentre" = var.billing_code
  }
}
