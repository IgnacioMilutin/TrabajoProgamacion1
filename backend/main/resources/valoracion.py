from flask_restful import Resource
from flask import request, jsonify
from main.models import ResenasModel, UsuarioModel, LibroModel
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Resena(Resource):
    @jwt_required(optional=True)
    def get(self,id_resena):
        resena=db.session.query(ResenasModel).get_or_404(id_resena)
        return resena.to_json()
    
    @role_required(roles=["admin"])
    def delete(self,id_resena):
        resena=db.session.query(ResenasModel).get_or_404(id_resena)
        db.session.delete(resena)
        db.session.commit()
        return 'reseña eliminada correctamente', 204

class Resenas(Resource):
    @jwt_required(optional=True)
    def get(self):
        page=1
        per_page=10
        resenas=db.session.query(ResenasModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        if request.args.get('id_usuario'):
            resenas=resenas.outerjoin(UsuarioModel).filter(UsuarioModel.id_usuario==(request.args.get('id_usuario')))
        if request.args.get('id_libro'):
            resenas=resenas.outerjoin(LibroModel).filter(LibroModel.id_libro==(request.args.get('id_libro')))
        resenas=resenas.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'resenas': [resena.to_json() for resena in resenas],
                  'total': resenas.total,
                  'pages': resenas.pages,
                  'page': page
                })
    
    @jwt_required()
    def post(self):
        resena=ResenasModel.from_json(request.get_json())
        db.session.add(resena)
        db.session.commit()
        return resena.to_json(), 201
    