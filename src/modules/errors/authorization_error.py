from werkzeug.exceptions import HTTPException


class AuthorizationError(HTTPException):
        """
        Exception when try authorize User
        """
        code = 401
