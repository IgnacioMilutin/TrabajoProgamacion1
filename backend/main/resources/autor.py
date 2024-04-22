from flask_restful import Resource
from flask import request, jsonify
from main.models import AutorModel
from .. import db

class Autor(Resource):
    def get(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        return autor.to_json()
    
    def delete(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        db.session.delete(autor)
        db.session.commit()
        return 'autor eliminado correctamente', 204
    
    def put(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        data=request.get_json().items()
        for key, value in data:
            setattr(autor,key,value)
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201

class Autores(Resource):
    def get(self):
        autores=db.session.query(AutorModel).all()
        return jsonify([autor.to_json() for autor in autores])
    def post(self):
        autor=AutorModel.from_json(request.get_json())
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
