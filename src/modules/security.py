from operator import eq
from os import environ
from time import time

from jose import JWTError, jwt
from six import raise_from
from werkzeug.exceptions import Unauthorized

from modules.error_types import AuthorizationError


def decode_token(token):
    """Try decode Bearer Token to JsonObject
        params:
        - token -> bearer token
    """
    try:
        return jwt.decode(token, environ['JWT_SECRET'], environ['JWT_ALGORITM'])
    except JWTError as e:
        raise_from(Unauthorized, e)


def generate_token(user_document) -> str:
    """
    Create Bearer token by UserLogin
    :type user_document: UserModel - UserModel Document object
    :rtype: str
    :return: Bearer Token
    """

    if eq(user_document, None):
        raise AuthorizationError(description='UserModel login or password is invalid!')
    else:
        time_ticks = int(time())
        payload = {
            "iss": environ['JWT_ISSUER'],
            "iat": time_ticks,
            "exp": time_ticks + int(environ['JWT_TOKEN_EXPIRATION_SECONDS']),
            "sub": user_document['login'],
            "claims": {
                "role": user_document['role']
            }
        }
        return jwt.encode(payload, environ['JWT_SECRET'])

