from connexion import FlaskApp
from connexion.exceptions import Unauthorized
from src.modules.error_handlers import unauthorized_error_handler


app = FlaskApp(__name__,specification_dir='swagger/')
app.add_api('timers_api_documentation.yaml')
app.add_error_handler(Unauthorized, unauthorized_error_handler)

if __name__ == '__main__':
    app.run(port=8080,debug=True,use_reloader=True,threaded=False)
