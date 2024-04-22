from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

NOTIFICACIONES={
    1:{'user_id':'1','fecha':'27/03/24','hora':'13:45','mensaje':'Prestamo aceptado'}
}

class Notificacion(Resource):
    def get(self):
        notificaciones=db.session.query(NotificacionModel).all()
        return jsonify([notificacion.to_json() for notificacion in notificaciones])
    def post(self):
        notificacion=NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
