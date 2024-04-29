from flask_restful import Resource
from flask import request, jsonify
from main.models import LibroModel, AutorModel, libros_autoresModel
from .. import db

class Libro(Resource):
    def get(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        return libro.to_json()
    
    def delete(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        db.session.delete(libro)
        db.session.commit()
        return 'libro eliminado correctamente', 204
    
    def put(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        data=request.get_json().items()
        for key, value in data:
            setattr(libro,key,value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201

class Libros(Resource):
    def get(self):
        libros=db.session.query(LibroModel).all()
        return jsonify([libro.to_json() for libro in libros])
    def post(self):
        librodata=request.get_json()
        autores_ids=librodata.get('autores')
        libro=LibroModel.from_json(librodata)
        db.session.add(libro)
        db.session.commit()
        if autores_ids:
            autores = AutorModel.query.filter(AutorModel.id_autor.in_(autores_ids)).all()
            for autor in autores:
                libro.autores.append(autor)
        db.session.commit()
        return libro.to_json(), 201

        