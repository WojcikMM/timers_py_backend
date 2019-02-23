from connexion import FlaskApp
from flask_injector import FlaskInjector
from mongoengine import connect

from modules.configurations.dependencies import configure_dependencies
from modules.configurations.error_handlers import configure_error_handlers

app = FlaskApp(__name__, specification_dir='swagger/')
app.add_api('timers_api_documentation.yaml', strict_validation=True)
app = configure_error_handlers(app=app)
FlaskInjector(app=app.app, modules=[configure_dependencies])

if __name__ == '__main__':
    connect('timers', host='localhost', port=27017)
    app.run(port=8080, debug=True, use_reloader=True, threaded=False)
