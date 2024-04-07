from flask_restful import Resource
from flask import request

CONFIGURACION={
    1:{"nombre_config":"tema","estado":"oscuro"}
}


class Configuraciones(Resource):
    def get(self):
        return CONFIGURACION, 200

class Configuracion(Resource):
    def get(self,id):
        if int(id) in CONFIGURACION:
            return CONFIGURACION[int(id)]
        return 'No existe el id', 404
    
    def put(self,id):
        if int(id) in CONFIGURACION:
            config=CONFIGURACION[int(id)]
            data=request.get_json()
            config.update(data)
            return '',201
        return 'No existe el id',404