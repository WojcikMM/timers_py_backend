from os import environ
from connexion import FlaskApp
from mongoengine import connect
from modules.error_handlers import configure_error_handlers

app_is_debug_mode = environ['FLASK_IS_DEBUG'] == 'True'
app_use_reloader = environ['FLASK_USE_RELOADER'] == 'True'

app = FlaskApp(__name__, specification_dir='swagger/')
app = configure_error_handlers(app=app)
app.add_api('timers_api_documentation.yaml', strict_validation=True)

if __name__ == '__main__':
    connect(environ['MONGO_DATABASE_NAME'], host=environ['MONGO_DATABASE_SERVER'], port=int(environ['MONGO_DATABASE_PORT']))
    app.run(port=int(environ['FLASK_DEFAULT_PORT']), debug=app_is_debug_mode, use_reloader=app_use_reloader, threaded=False)
