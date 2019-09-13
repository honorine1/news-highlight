from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from config import DevConfig

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extension

    bootstrap.init_app(app)

    #Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setting config
    from .requests import configure_request
    configure_request(app)

    #initialize flask extension
    bootstrap = Bootstrap(app)
     # Will add the views and forms

    

    return app


# Initializing application
#app = Flask(__name__, instance_relative_config = True) instance_relative_config = True is added to connect to the instance when the app instance is created

# Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py') # this connects to the config.py file and all its contents are appended to the app.config

# from app import views