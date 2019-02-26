from werkzeug.exceptions import HTTPException


class AuthorizationError(HTTPException):
        """
        Exception when try authorize UserModel
        """
        code = 401
