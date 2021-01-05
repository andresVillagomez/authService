from flask_restplus import Namespace, fields

class MainDto:
    api = Namespace('Auth', description='Operaciones relacionadas a la autenticación y autorización de usuarios')

    user_auth = api.model('Parametros de autenticación', {
        'email': fields.String(required=True, description='Correo electrónico del usuario', example="example@domain.com"),
        'password': fields.String(required=True, description='Contraseña', example="1234567890")
    })