from flask_restful import Resource
from flask import request

PRESTAMOS={
    1:{'usuario_id':'1','libro':'El Gato Negro'},
    2:{'usuario_id':'2','libro':'Ficciones'}
}

class Prestamo(Resource):
    def get(self,id):
        if int(id) in PRESTAMOS:
            return  PRESTAMOS[int(id)]
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS[int(id)]
            return '',204
        return 'No existe el id',404
    
    def put(self,id):
        if int(id) in PRESTAMOS:
            prestamo=PRESTAMOS[int(id)]
            data=request.get_json()
            prestamo.update(data)
            return '',201
        return 'No existe el id',404

class Prestamos(Resource):
    def get(self):
        return PRESTAMOS
    def post(self):
        prestamo=request.get_json()
        id=int(max(PRESTAMOS.keys()))+1
        PRESTAMOS[id]=prestamo
        return PRESTAMOS[id],201
