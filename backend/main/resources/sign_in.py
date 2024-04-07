from flask_restful import Resource
from flask import request
from .usuario import USUARIOS

class sign_in(Resource):
    def post(self):
            nuevo=request.get_json()
            id=int(max(USUARIOS.keys()))+1
            USUARIOS[id]=nuevo
            return USUARIOS[id],201
    
class log_in(Resource):
    def post(self,nombre,contrasena):
        for usuario_id, usuario_data in USUARIOS.items():
            if usuario_data['nombre']==nombre and usuario_data['contrasena']==contrasena:
                return {'usuario_id':usuario_id}, 200
        return 'usuario no disponible', 404