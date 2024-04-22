from flask_restful import Resource
from flask import request
from .. import db
from main.models import UsuarioModel

class sign_in(Resource):
    def post(self):
        usuario=UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
       
# class log_in(Resource):
#     def post(self,nombre,contrasena):
#         for usuario_id, usuario_data in USUARIOS.items():
#             if usuario_data['nombre']==nombre and usuario_data['contrasena']==contrasena:
#                 return {'usuario_id':usuario_id}, 200
#         return 'usuario no disponible', 404