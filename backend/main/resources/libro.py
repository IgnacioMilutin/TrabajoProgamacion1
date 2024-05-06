from flask_restful import Resource
from flask import request, jsonify
from main.models import LibroModel, AutorModel, libros_autoresModel, libros_prestamosModel
from .. import db
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Libro(Resource):

    @jwt_required(optional=True)
    def get(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        return libro.to_json()
    
    @role_required(roles=["admin"])
    def delete(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        db.session.delete(libro)
        db.session.commit()
        return 'libro eliminado correctamente', 204

    @role_required(roles=["admin"])
    def put(self,id_libro):
        libro=db.session.query(LibroModel).get_or_404(id_libro)
        data=request.get_json().items()
        for key, value in data:
            setattr(libro,key,value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201

class Libros(Resource):

    @jwt_required(optional=True)
    def get(self):
        page=1
        per_page=10
        libros=db.session.query(LibroModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        if request.args.get('genero'):
            libros=libros.filter(LibroModel.genero.like("%"+request.args.get('genero')+"%"))
        if request.args.get('activo'):
            libros=libros.filter(LibroModel.activo.like("%"+request.args.get('activo')+"%"))
        if request.args.get('editorial'):
            libros=libros.filter(LibroModel.editorial.like("%"+request.args.get('editorial')+"%"))
        if request.args.get('valoracion_positiva'):
            libros=libros.filter(LibroModel.valoracion_total>=3)
        if request.args.get('valoracion_negativa'):
            libros=libros.filter(LibroModel.valoracion_total<3)
        if request.args.get('valoracion_mayorigual_a'):
            libros=libros.filter(LibroModel.valoracion_total>=request.args.get('valoracion_mayorigual_a'))
        #revisar
        if request.args.get('mayor_prestamos'):
            libros=db.session.query(LibroModel, func.count(libros_prestamosModel.c.id_libro).join(libros_prestamosModel).group_by(LibroModel.id_libro).order_by(func.count(libros_prestamosModel.c.id_libro).desc()))
        libros=libros.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'libros': [libro.to_json() for libro in libros],
                  'total': libros.total,
                  'pages': libros.pages,
                  'page': page
                })
    
    @role_required(roles=["admin"])
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

        