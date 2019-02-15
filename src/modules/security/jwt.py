from time import time
from jose import JWTError, jwt
from six import raise_from
from werkzeug.exceptions import Unauthorized
from os import environ
from modules.security.secrets_reader import get_secret


def decode_token(token):
    """Try decode Bearer Token to JsonObject
        params:
        - token -> bearer token
    """
    try:
        return jwt.decode(token,
                          get_secret(environ['JWT_SECRETS'], 'JWT_SECRET'),
                          get_secret(environ['JWT_SECRETS'], 'JWT_ALGORITM'))
    except JWTError as e:
        raise_from(Unauthorized, e)


def generate_token(login)-> str:
    """
    Create Bearer token by UserLogin
    :param login: userLogin
    :return: Bearer Token
    """
    time_ticks = int(time())
    payload = {
        "iss": get_secret(environ['JWT_SECRETS'], 'JWT_ISSUER'),
        "iat": time_ticks,
        "exp": time_ticks + get_secret(environ['JWT_SECRETS'], 'JWT_TOKEN_EXPIRATION_SECONDS'),
        "sub": login,
        "claims": {
            "roles": ["user", "actionReader"]
        }
    }
    return jwt.encode(payload, get_secret(environ['JWT_SECRETS'], 'JWT_SECRET'))
