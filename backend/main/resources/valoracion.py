from flask_restful import Resource
from flask import request, jsonify
from main.models import ResenasModel
from .. import db

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
    def get(self):
        resenas=db.session.query(ResenasModel).all()
        return jsonify([resena.to_json() for resena in resenas])

    def post(self):
        resena=ResenasModel.from_json(request.get_json())
        db.session.add(resena)
        db.session.commit()
        return resena.to_json(), 201

class Resenas_por_usuario(Resource):
    def get(self,id_usuario):
        resenas=db.session.query(ResenasModel)
        resenas=resenas.filter(ResenasModel.id_usuario==id_usuario)
        resenas=resenas.all()
        return jsonify({'resenas':[resena.to_json() for resena in resenas]})
    
class Resenas_por_libro(Resource):
    def get(self,id_libro):
        resenas=db.session.query(ResenasModel)
        resenas=resenas.filter(ResenasModel.id_libro==id_libro)
        resenas=resenas.all()
        return jsonify({'resenas':[resena.to_json() for resena in resenas]})
    