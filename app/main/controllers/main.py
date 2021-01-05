from flask import request, jsonify
from flask_restplus import Resource, fields
from ..utils.dto import MainDto

api = MainDto.api

@api.route('/login')
class UserLogin(Resource):
    @api.doc(description='Iniciar sesión en el sistema')
    @api.expect(MainDto.user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return jsonify(post_data)