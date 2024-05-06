from flask_restful import Resource
from flask import request, jsonify
from main.models import PrestamoModel, LibroModel, libros_prestamosModel,UsuarioModel
from .. import db
from sqlalchemy import func, desc
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Prestamo(Resource):

    @jwt_required()
    def get(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        return prestamo.to_json()
    
    @role_required(roles=["admin"])
    def delete(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        db.session.delete(prestamo)
        db.session.commit()
        return 'prestamo eliminado correctamente', 204
    
    @role_required(roles=["admin"])
    def put(self,id_prestamo):
        prestamo=db.session.query(PrestamoModel).get_or_404(id_prestamo)
        data=request.get_json().items()
        for key, value in data:
            setattr(prestamo,key,value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201
    
class Prestamos(Resource):

    @jwt_required()
    def get(self):
        page=1
        per_page=10
        prestamos=db.session.query(PrestamoModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        if request.args.get('fecha_inicio'):
            prestamos=prestamos.filter(PrestamoModel.fecha_inicio.like(datetime.datetime.strptime(request.args.get('fecha_inicio'),'%d-%m-%Y')))
        if request.args.get('fecha_limite'):
            prestamos=prestamos.filter(PrestamoModel.fecha_limite.like(datetime.datetime.strptime(request.args.get('fecha_limite'),'%d-%m-%Y')))
        if request.args.get('prestamo_activo'):
            fecha_str=datetime.datetime.now().strftime("%d-%m-%Y")
            fecha_datetime=datetime.datetime.strptime(fecha_str,'%d-%m-%Y')
            prestamos=prestamos.filter(PrestamoModel.fecha_limite>=fecha_datetime)
        if request.args.get('prestamo_finalizado'):
            fecha_str=datetime.datetime.now().strftime("%d-%m-%Y")
            fecha_datetime=datetime.datetime.strptime(fecha_str,'%d-%m-%Y')
            prestamos=prestamos.filter(PrestamoModel.fecha_limite<fecha_datetime)
        if request.args.get('id_libro'):
            prestamos=prestamos.outerjoin(libros_prestamosModel).filter(libros_prestamosModel.c.id_libro==(request.args.get('id_libro')))
        if request.args.get('id_usuario'):
            prestamos=prestamos.outerjoin(UsuarioModel).filter(UsuarioModel.id_usuario==(request.args.get('id_usuario')))
        prestamos=prestamos.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'prestamos': [prestamo.to_json() for prestamo in prestamos],
                  'total': prestamos.total,
                  'pages': prestamos.pages,
                  'page': page
                })
    

    @role_required(roles=["admin"])
    def post(self):
        prestamodata=request.get_json()
        libros_ids=prestamodata.get('libros')
        prestamo=PrestamoModel.from_json(prestamodata)
        db.session.add(prestamo)
        db.session.commit()
        if libros_ids:
            libros = LibroModel.query.filter(LibroModel.id_libro.in_(libros_ids)).all()
            for libro in libros:
                prestamo.libros.append(libro)
        db.session.commit()
        return prestamo.to_json(), 201
