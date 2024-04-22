from flask_restful import Resource
from flask import request, jsonify
from main.models import ResenasModel
from .. import db

VALORACION={
    1:{'libro_id':'El Gato Negro','puntuacion':'4.5','comentario':'Muy bueno'}
}

class Resena(Resource):
    def get(self,id_resena):
        resena=db.session.query(ResenasModel).get_or_404(id_resena)
        return resena.to_json()
    
    def delete(self,id_resena):
        resena=db.session.query(ResenasModel).get_or_404(id_resena)
        db.session.delete(resena)
        db.session.commit()
        return 'reseña eliminada correctamente', 204

class Resenas(Resource):    
    def post(self):
        resena=ResenasModel.from_json(request.get_json())
        db.session.add(resena)
        db.session.commit()
        return resena.to_json(), 201
