from connexion import request
from src.modules.security.jwt import generate_token


def login_user() -> {dict, int}:
    """Authorize user and return json object with Bearer Token"""
    return {'token': generate_token(request.json['login'])}, 200


def register_user() -> {dict, int}:
    """
    Register new user to application
    :return:
    """
    return {'token': generate_token(request.json['login'])}, 200
