import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DYNAMODB_TABLE = os.environ.get('DYNAMODB_TABLE', 'PasswordManager')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")

    http_method = event.get('httpMethod')
    path = event.get('path')

    if http_method == 'POST':
        return store_password(event)
    elif http_method == 'GET':
        return retrieve_password(event)
    else:
        return response(400, {"error": "Invalid path or method"})

def store_password(event):
    try:
        body = json.loads(event.get('body', '{}'))
        service = body.get('service')
        username = body.get('username')
        password_hash = body.get('password')

        if not service or not username or not password_hash:
            return response(400, {"error": "Service, username, and hashed password are required"})

        # Directly store hashed password sent from client
        table.put_item(Item={
            'service': service,
            'username': username,
            'password_hash': password_hash
        })

        logger.info(f"Stored credentials for service: {service}")
        return response(200, {"message": f"Credentials stored for service '{service}'"})

    except Exception as e:
        logger.error(f"Error storing password: {str(e)}")
        return response(500, {"error": "Internal server error"})

def retrieve_password(event):
    try:
        query_params = event.get('queryStringParameters') or {}
        service = query_params.get('service')

        logger.info(f"retrieving credentials for service: {service}")
        if not service:
            return response(400, {"error": "Service name is required in query string"})

        result = table.get_item(Key={'service': service})

        if 'Item' not in result:
            return response(404, {"error": "Service not found"})

        return response(200, {
            "service": service,
            "username": result['Item']['username'],
            "password_hash": result['Item']['password_hash']
        })

    except Exception as e:
        logger.error(f"Error retrieving password: {str(e)}")
        return response(500, {"error": "Internal server error"})

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
