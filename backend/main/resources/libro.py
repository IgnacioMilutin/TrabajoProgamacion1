from flask_restful import Resource
from flask import request, jsonify
from main.models import LibroModel
from .. import db

LIBROS={
    1:{'titulo':'El Gato Negro','autor':'Edgar Allan Poe','genero':'ficcion gotica'},
    2:{'titulo':'Ficciones','autor':'Jorge Luis Borgees', 'genero':'literatura fantastica'}
}
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
        libro=LibroModel.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201