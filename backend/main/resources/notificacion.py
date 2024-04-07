from flask_restful import Resource
from flask import request

NOTIFICACIONES={
    1:{'user_id':'1','fecha':'27/03/24','hora':'13:45','mensaje':'Prestamo aceptado'}
}

class Notificacion(Resource):
    def post(self):
        nuevo=request.get_json()
        id=int(max(NOTIFICACIONES.keys()))+1
        NOTIFICACIONES[id]=nuevo
        return NOTIFICACIONES[id],201