from werkzeug.exceptions import HTTPException


class IncorrectAuthorizeArgumentError(HTTPException):
    """
    Exception when try authorize UserModel
    """
    description = "You use authorization decorator on action with no token authorization"
    code = 500

