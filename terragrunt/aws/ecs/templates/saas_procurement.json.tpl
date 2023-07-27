[
    "image": "${image}",
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
  }
]
