from flask import Response
from json import dumps


def unauthorized_error_handler(exception: Exception) -> Response:
    return Response(response=dumps({"message": "Bad Bearer Token. You are not authorized."}), status=401,
                    mimetype="application/json")


def fail_validation_handler(exception: Exception)->Response:
    return Response(response=dumps({'validationMessages': ('message1', 'message2', 'message3')}), status=400,
                    mimetype="application/json")
