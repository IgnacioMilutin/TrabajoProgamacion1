from flask_restful import Resource
from flask import request, jsonify
from main.models import PrestamoModel, LibroModel
from .. import db

class Prestamo(Resource):
    def get(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        return prestamo.to_json()
    
    def delete(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        db.session.delete(prestamo)
        db.session.commit()
        return 'prestamo eliminado correctamente', 204
    
    def put(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        data=request.get_json().items()
        for key, value in data:
            setattr(prestamo,key,value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201
    
class Prestamos(Resource):
    def get(self):
        prestamos=db.session.query(PrestamoModel).all()
        return jsonify([prestamo.to_json() for prestamo in prestamos])
    def post(self):
        libros_ids=request.get_json().get('libros')
        prestamo=PrestamoModel.from_json(request.get_json())
        if libros_ids:
            libros=LibroModel.query.filter(LibroModel.id_libro.in_(libros_ids)).all()
            prestamo.libros.extend(libros)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201

class Prestamos_por_usuario(Resource):
    def get(self,id_usuario):
        prestamos=db.session.query(PrestamoModel)
        prestamos=prestamos.filter(PrestamoModel.id_usuario==id_usuario)
        prestamos=prestamos.all()
        return jsonify({'prestamos':[prestamo.to_json() for prestamo in prestamos]})

class Prestamos_por_libro(Resource):
    def get(self,id_libro):
        prestamos=db.session.query(PrestamoModel)
        prestamos=prestamos.filter(PrestamoModel.id_libro==id_libro)
        prestamos=prestamos.all()
        return jsonify({'prestamos':[prestamo.to_json() for prestamo in prestamos]})
