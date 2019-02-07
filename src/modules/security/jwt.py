from time import time
from jose import JWTError, jwt
from six import raise_from
from werkzeug.exceptions import Unauthorized

from src.config import jwt_settings


def decode_token(token):
    """Try decode Bearer Token to JsonObject
        params:
        - token -> bearer token
    """
    try:
        return jwt.decode(token, jwt_settings['secret'], jwt_settings['algorithm'])
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
        "iss": jwt_settings['issuer'],
        "iat": time_ticks,
        "exp": time_ticks + jwt_settings['expiration_time_seconds'],
        "sub": login,
        "claims": {
            "roles": ["user", "actionReader"]
        }
    }
    return jwt.encode(payload, jwt_settings['secret'])
