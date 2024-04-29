from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

class Notificacion(Resource):
    def get(self):
        notificaciones=db.session.query(NotificacionModel).all()
        return jsonify([notificacion.to_json() for notificacion in notificaciones])
                       
    def post(self):
        notificacion=NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
    
class Notificacion_por_usuario(Resource):
    def get(self,id_usuario):
        notificaciones=db.session.query(NotificacionModel)
        notificaciones=notificaciones.filter(NotificacionModel.id_usuario==id_usuario)
        notificaciones=notificaciones.all()
        return jsonify({'notificaciones':[notificacion.to_json() for notificacion in notificaciones]})