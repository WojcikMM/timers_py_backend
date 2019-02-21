from werkzeug.exceptions import HTTPException


class IncorrectAuthorizeArgumentError(HTTPException):
    """
    Exception when try authorize User
    """
    description = "You use authorization decorator on action with no token authorization"
    code = 500

