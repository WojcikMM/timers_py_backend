from functools import wraps

from modules.errors.authorization_error import AuthorizationError
from modules.errors.incorrect_authorize_argument_error import IncorrectAuthorizeArgumentError


class AuthorizeAttribute(object):
    def __init__(self, required_roles: [str]):
        """Attribute that guarantees only authorized access for users with the required "required_role" role"""
        self.__required_roles = required_roles

    def __call__(self, function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            if 'token_info' not in kwargs:
                raise IncorrectAuthorizeArgumentError(
                    description="You use authorization decorator on action with no token authorization")
            elif 'role' not in kwargs['token_info']:
                raise IncorrectAuthorizeArgumentError(description="You don't have any authorization roles")
            else:
                if kwargs['token_info']['role'] is not self.__required_roles:
                    raise AuthorizationError(description="You don,t have required role to do this action.")
                else:
                    return function(*args, **kwargs)

        return wrapped_function
