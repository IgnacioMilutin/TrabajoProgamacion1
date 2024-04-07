from flask_restful import Resource
from flask import request
USUARIOS={
    1:{'nombre':'Peter','contrasena':'chau'},
    2:{'nombre':'Boby','contrasena':'hola'}
}

class Usuario(Resource):
    def get(self,id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return '',204
        return 'No existe el id',404
    
    def put(self,id):
        if int(id) in USUARIOS:
            usuario=USUARIOS[int(id)]
            data=request.get_json()
            usuario.update(data)
            return '',201
        return 'No existe el id',404

class Usuarios(Resource):
    def get(self):
        return USUARIOS
    def post(self):
        usuario=request.get_json()
        id=int(max(USUARIOS.keys()))+1
        USUARIOS[id]=usuario
        return USUARIOS[id],201