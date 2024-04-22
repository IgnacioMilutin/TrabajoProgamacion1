from flask_restful import Resource
from flask import request, jsonify
from main.models import UsuarioModel
from .. import db

USUARIOS={
    1:{'nombre':'Peter','contrasena':'chau'},
    2:{'nombre':'Boby','contrasena':'hola'}
}

class Usuario(Resource):
    def get(self,id_usuario):
        usuario=db.session.query(UsuarioModel).get_or_404(id_usuario)
        return usuario.to_json()
    
    def delete(self,id_usuario):
        usuario=db.session.query(UsuarioModel).get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'usuario eliminado correctamente', 204
    
    def put(self,id_usuario):
        usuario=db.session.query(UsuarioModel).get_or_404(id_usuario)
        data=request.get_json().items()
        for key, value in data:
            setattr(usuario,key,value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

class Usuarios(Resource):
    def get(self):
        usuarios=db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    def post(self):
        usuario=UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201