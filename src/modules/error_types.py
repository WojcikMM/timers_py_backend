from werkzeug.exceptions import HTTPException


class AuthorizationError(HTTPException):
    """
        Exception when try authorize UserModel
        """
    code = 401


class IncorrectAuthorizeArgumentError(HTTPException):
    """
    Exception when try authorize UserModel
    """
    description = "You use authorization decorator on action with no token authorization"
    code = 500


class InvalidConfigurationArgumentError(Exception):
    def __init__(self, env_key: str):
        """
        Exception when try read enviroment variable but it not exists.
        :type env_key: Enviroment variable key name
        """
        self.env_key = env_key
