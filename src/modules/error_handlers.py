from json import dumps

from connexion import FlaskApp
from flask import Response
from mongoengine import DoesNotExist

from modules.error_types import IncorrectAuthorizeArgumentError


def configure_error_handlers(app: FlaskApp):
    app.add_error_handler(401, unauthorized_error_handler)
    app.add_error_handler(403, authorization_error_handler)
    app.add_error_handler(IncorrectAuthorizeArgumentError, authorization_error_handler)
    app.add_error_handler(500, internal_error_handler)
    app.add_error_handler(DoesNotExist, not_found_error)
    return app


def not_found_error(exception) -> Response:
    print(exception)
    return Response(response=dumps({"message": "No records found for your searching criteria."}), status=404,
                    mimetype="application/json")


def unauthorized_error_handler(exception) -> Response:
    print(exception)
    return Response(response=dumps({"message": "Bad Bearer Token. You are not authorized."}), status=401,
                    mimetype="application/json")


def authorization_error_handler(exception) -> Response:
    return Response(response=dumps({"message": exception.description}), status=exception.code,
                    mimetype="application/json")


def internal_error_handler(exception) -> Response:
    print(exception)
    return Response(response=dumps({"message": "Document exists jet in database. "}), status=400,
                    mimetype="application/json")
