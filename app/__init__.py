from flask_restplus import Api
from flask import Blueprint

from .main.controllers.main import api as main_ns

blueprint = Blueprint('authService', __name__)

api = Api(blueprint, title='Authentication Services', version='1.0', description='Servicios de autenticación')


api.add_namespace(main_ns, path='/auth')