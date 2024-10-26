import requests
from functools import wraps
from flask import jsonify, request

from utils import credentials

def validate_token(func):
    def verify_token(token):
        credentials_dd = credentials.server_configuration()
        auth_server_url = credentials_dd["auth_server_url"]
        cleaned_auth_server_url = auth_server_url + "protected"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(cleaned_auth_server_url, headers=headers)
        return response.status_code == 200

    @wraps(func)

    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get('Authorization').split(" ")[1]
        except Exception as _:
            return jsonify({'message': 'No token provided'}), 401

        if not verify_token(token):
            return jsonify({'message': 'Invalid Token'}), 401

        return func(*args, **kwargs)

    return wrapper

