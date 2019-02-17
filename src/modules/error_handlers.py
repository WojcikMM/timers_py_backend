from json import dumps

from flask import Response
from werkzeug.exceptions import HTTPException


def unauthorized_error_handler(exception) -> Response:
    return Response(response=dumps({"message": "Bad Bearer Token. You are not authorized."}), status=401,
                    mimetype="application/json")


def authorization_error_handler(exception) -> Response:
    return Response(response=dumps({"message": exception.description}), status=exception.code, mimetype="application/json")


def fail_validation_handler() -> Response:
    return Response(response=dumps({'validationMessages': ('message1', 'message2', 'message3')}), status=400,
                    mimetype="application/json")
