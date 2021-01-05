import logging
from flask import Flask

from .config import config_by_name

logging.basicConfig()

# initializes basic server configuration
def create_app(config_name):
    app = Flask(__name__, static_folder='/static')
    app.config.from_object(config_by_name[config_name])
    return app