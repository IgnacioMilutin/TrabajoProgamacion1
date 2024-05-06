from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel, UsuarioModel
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Notificacion(Resource):
    @jwt_required()
    def get(self):
        page=1
        per_page=10
        notificaciones=db.session.query(NotificacionModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        if request.args.get('entregado'):
            notificaciones=notificaciones.filter(NotificacionModel.entregado.like("%"+request.args.get('entregado')+"%"))
        if request.args.get('id_usuario'):
            notificaciones=notificaciones.outerjoin(UsuarioModel).filter(UsuarioModel.id_usuario==(request.args.get('id_usuario')))
        notificaciones=notificaciones.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'notificaciones': [notifacion.to_json() for notifacion in notificaciones],
                  'total': notificaciones.total,
                  'pages': notificaciones.pages,
                  'page': page
                })

    @role_required(roles=["admin"])                   
    def post(self):
        notificacion=NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
    