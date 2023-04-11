import boto3

# Generate .env file from AWS parameter store
ssm = boto3.client('ssm', region_name='ca-central-1')
saas_app_config = ssm.get_parameter(Name='saas_app_config', WithDecryption=True)['Parameter']['Value']
env_file = open('.env', 'w')
env_file.write(saas_app_config)
env_file.close()
