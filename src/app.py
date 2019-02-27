from os import environ

from connexion import FlaskApp
from flask_injector import FlaskInjector
from mongoengine import connect

from modules.configurations.dependencies import configure_dependencies
from modules.configurations.error_handlers import configure_error_handlers

mongo_database_name = environ['MONGO_DATABASE_NAME']
mongo_database_server = environ['MONGO_DATABASE_SERVER']

app_default_port = environ['FLASK_DEFAULT_PORT']
app_is_debug_mode = environ['FLASK_IS_DEBUG']
app_use_reloader = environ['FLASK_USE_RELOADER']

app = FlaskApp(__name__, specification_dir='swagger/')
app.add_api('timers_api_documentation.yaml', strict_validation=True)
app = configure_error_handlers(app=app)
FlaskInjector(app=app.app, modules=[configure_dependencies])

if __name__ == '__main__':
    connect(mongo_database_name, host=mongo_database_server, port=app_default_port)
    app.run(port=app_default_port, debug=app_is_debug_mode, use_reloader=app_use_reloader, threaded=False)
