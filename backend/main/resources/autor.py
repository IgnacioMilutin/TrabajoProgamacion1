from flask_restful import Resource
from flask import request, jsonify
from main.models import AutorModel
from .. import db
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Autor(Resource):
    @jwt_required(optional=True)
    def get(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        return autor.to_json()
    
    @role_required(roles=["admin"])
    def delete(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        db.session.delete(autor)
        db.session.commit()
        return 'autor eliminado correctamente', 204
    
    @role_required(roles=["admin"])
    def put(self,id_autor):
        autor=db.session.query(AutorModel).get_or_404(id_autor)
        data=request.get_json().items()
        for key, value in data:
            setattr(autor,key,value)
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201

class Autores(Resource):
    @jwt_required(optional=True)
    def get(self):
        page=1
        per_page=10
        autores=db.session.query(AutorModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        autores=autores.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'autores': [autor.to_json() for autor in autores],
                  'total': autores.total,
                  'pages': autores.pages,
                  'page': page
                })
    
    @role_required(roles=["admin"])
    def post(self):
        autor=AutorModel.from_json(request.get_json())
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
