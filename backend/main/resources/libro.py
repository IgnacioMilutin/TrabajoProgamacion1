from flask_restful import Resource
from flask import request

LIBROS={
    1:{'titulo':'El Gato Negro','autor':'Edgar Allan Poe','genero':'ficcion gotica'},
    2:{'titulo':'Ficciones','autor':'Jorge Luis Borgees', 'genero':'literatura fantastica'}
}
class Libro(Resource):
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        return 'No existe el id', 404
    
    def delete(self,id):
        if int(id) in LIBROS:
            del LIBROS[int(id)]
            return '',204
        return 'No existe el id',404
    
    def put(self,id):
        if int(id) in LIBROS:
            libro=LIBROS[int(id)]
            data=request.get_json()
            libro.update(data)
            return '',201
        return 'No existe el id',404

class Libros(Resource):
    def get(self):
        return LIBROS
    def post(self):
        libro=request.get_json()
        id=int(max(LIBROS.keys()))+1
        LIBROS[id]=libro
        return LIBROS[id],201