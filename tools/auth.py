from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import jsonify, request
from tools.kms import get_secret
import json

# auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(username, password):
#     if not request.path.startswith('/v1/'):
#         return True

#     HTTP_CREDENTIALS = get_secret('HTTP_CREDENTIALS');
#     credentials = json.loads(HTTP_CREDENTIALS);
#     return username in credentials and credentials[username] == password

auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def verify_token(token):
    if not request.path.startswith('/v1/'):
        return True
    
    credentials = get_secret('HTTP_CREDENTIALS')
    return token == credentials

@auth.error_handler
def auth_error():
    # 在认证失败时调用此函数
    return jsonify({'message': 'Access denied: authentication failed'}), 403