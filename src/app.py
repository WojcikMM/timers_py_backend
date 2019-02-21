from connexion import FlaskApp
from connexion.exceptions import Unauthorized
from flask_injector import FlaskInjector
from modules.dependencies_configuration.dependencies import configure_dependencies
from modules.error_handlers import unauthorized_error_handler, authorization_error_handler
from modules.errors.authorization_error import AuthorizationError
from modules.errors.incorrect_authorize_argument_error import IncorrectAuthorizeArgumentError

app = FlaskApp(__name__, specification_dir='swagger/')
app.add_api('timers_api_documentation.yaml', strict_validation=True)

app.add_error_handler(Unauthorized, unauthorized_error_handler)
app.add_error_handler(AuthorizationError, authorization_error_handler)
app.add_error_handler(IncorrectAuthorizeArgumentError, authorization_error_handler)
FlaskInjector(app=app.app, modules=[configure_dependencies])

if __name__ == '__main__':
    app.run(port=8080, debug=True, use_reloader=True, threaded=False)
