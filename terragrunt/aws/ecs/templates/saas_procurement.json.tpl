[
  {
    "image": "${image}",
    "linuxParameters": {
      "capabilities": {
        "drop": [
          "ALL"
        ]
      }
    },
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "${awslogs-group}",
        "awslogs-region": "${awslogs-region}",
        "awslogs-stream-prefix": "${awslogs-stream-prefix}"
      }
    },
    "name": "saas-procurement",
    "portMappings": [
 	{
	    "name": "saas-procurement-8000-tcp",
	    "containerPort": 8000,
	    "hostPort": 8000,
	    "protocol": "tcp",
    	    "appProtocol": "http"
	}
    ],
    "ulimits": [
      {
        "hardLimit": 1000000,
        "name": "nofile",
        "softLimit": 1000000
      }
    ]
  },
  "secrets": [
      {
        "name": "APPROVED_REQUEST_TEMPLATE_ID",
        "valueFrom": "${APPROVED_REQUEST_TEMPLATE_ID}"
      },
      {
        "name": "REQUEST_S32_APPROVED_TEMPLATE_ID",
        "valueFrom": "${REQUEST_S32_APPROVED_TEMPLATE_ID}"
      },
      {
        "name": "POSTGRES_PASSWORD",
        "valueFrom": "${POSTGRES_PASSWORD}"
      },
      {
        "name": "ENVIRONMENT",
        "valueFrom": "${ENVIRONMENT}"
      },
      {
        "name": "DJANGO_SECRET_KEY",
        "valueFrom": "${DJANGO_SECRET_KEY}"
      },
      {
        "name": "APPROVER_DELETE_TEMPLATE_ID",
        "valueFrom": "${APPROVER_DELETE_TEMPLATE_ID}"
      },
      {
        "name": "SOCIAL_APPLICATION_CLIENT_ID",
        "valueFrom": "${SOCIAL_APPLICATION_CLIENT_ID}"
      },
      {
        "name": "SAAS_SUBMISSION_TEMPLATE_ID",
        "valueFrom": "${SAAS_SUBMISSION_TEMPLATE_ID}"
      },
      {
        "name": "EDIT_REQUEST_TEMPLATE_ID",
        "valueFrom": "${EDIT_REQUEST_TEMPLATE_ID}"
      },
      {
        "name": "DELETE_SAAS_REQUEST_TEMPLATE_ID",
        "valueFrom": "${DELETE_SAAS_REQUEST_TEMPLATE_ID}"
      },
      {
        "name": "SAAS_SUBMISSION_EDIT_TEMPLATE_ID",
        "valueFrom": "${SAAS_SUBMISSION_EDIT_TEMPLATE_ID}"
      },
      {
        "name": "DENIED_REQUEST_TEMPLATE_ID",
        "valueFrom": "${DENIED_REQUEST_TEMPLATE_ID}"
      },
      {
        "name": "NOTIFY_URL",
        "valueFrom": "${NOTIFY_URL}"
      },
      {
        "name": "NOTIFY_API_KEY",
        "valueFrom": "${NOTIFY_API_KEY}"
      },
      {
        "name": "APPROVAL_REQUEST_TEMPLATE_ID",
        "valueFrom": "${APPROVAL_REQUEST_TEMPLATE_ID}"
      },
      {
        "name": "REQUEST_S32_DENIED_INTERNAL_OPS_TEMPLATE_ID",
        "valueFrom": "${REQUEST_S32_DENIED_INTERNAL_OPS_TEMPLATE_ID}"
      },
      {
        "name": "DB_HOST",
        "valueFrom": "${DB_HOST}"
      },
      {
        "name": "INTERNAL_OPS_REQUEST_MORE_INFO_TEMPLATE_ID",
        "valueFrom": "${INTERNAL_OPS_REQUEST_MORE_INFO_TEMPLATE_ID}"
      },
      {
        "name": "POSTGRES_USER",
        "valueFrom": "${POSTGRES_USER}"
      },
      {
        "name": "REQUEST_S32_DENIED_TEMPLATE_ID",
        "valueFrom": "${REQUEST_S32_DENIED_TEMPLATE_ID}"
      },
      {
        "name": "S32_APPROVAL_REQUESTED_TEMPLATE_ID",
        "valueFrom": "${S32_APPROVAL_REQUESTED_TEMPLATE_ID}"
      },
      {
        "name": "POSTGRES_DB",
        "valueFrom": "${POSTGRES_DB}"
      },
      {
        "name": "REQUEST_S32_APPROVED_INTERNAL_OPS_TEMPLATE_ID",
        "valueFrom": "${REQUEST_S32_APPROVED_INTERNAL_OPS_TEMPLATE_ID}"
      },
      {
        "name": "REQUESTOR_S32APPROVAL_PENDING_REVIEW_TEMPLATE_ID",
        "valueFrom": "${REQUESTOR_S32APPROVAL_PENDING_REVIEW_TEMPLATE_ID}"
      },
      {
        "name": "SOCIAL_APPLICATION_SECRET_KEY",
        "valueFrom": "${SOCIAL_APPLICATION_SECRET_KEY}"
      },
      {
        "name": "TESTING_FEATURE_FLAG",
        "valueFrom": "${TESTING_FEATURE_FLAG}"
      },
      {
        "name": "SITE_ID",
        "valueFrom": "${SITE_ID}"
      }
    ]

]
