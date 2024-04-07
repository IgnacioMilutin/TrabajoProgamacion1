from flask_restful import Resource
from flask import request

VALORACION={
    1:{'libro_id':'El Gato Negro','puntuacion':'4.5','comentario':'Muy bueno'}
}

class Valoracion(Resource):
    def get(self,id):
        if int(id) in VALORACION:
            return VALORACION[int(id)]
        return 'No existe el id', 404

class Valoraciones(Resource):    
    def post(self):
            val=request.get_json()
            id=int(max(VALORACION.keys()))+1
            VALORACION[id]=val
            return VALORACION[id],201
    
class Comentario(Resource):
    def get(self,id):
        if int(id) in VALORACION:
            return VALORACION[int(id)]
        return 'No existe el id', 404


class Comentarios(Resource):
    def post(self):
        val=request.get_json()
        id=int(max(VALORACION.keys()))+1
        VALORACION[id]=val
        return VALORACION[id],201