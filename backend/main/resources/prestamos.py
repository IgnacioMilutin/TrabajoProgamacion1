from flask_restful import Resource
from flask import request, jsonify
from main.models import PrestamoModel
from .. import db

PRESTAMOS={
    1:{'usuario_id':'1','libro':'El Gato Negro'},
    2:{'usuario_id':'2','libro':'Ficciones'}
}

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
        prestamo=PrestamoModel.from_json(request.get_json())
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201
