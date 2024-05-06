from flask_restful import Resource
from flask import request, jsonify
from main.models import UsuarioModel, PrestamoModel
from .. import db
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Usuario(Resource):

    @jwt_required(optional=True)
    def get(self,id_usuario):
        usuario=db.session.query(UsuarioModel).get_or_404(id_usuario)
        current_identity=get_jwt_identity()
        current_identity_role= db.session.query(UsuarioModel).filter_by(id_usuario=current_identity).first()
        current_identity_id = str(current_identity)
        id_usuario=str(id_usuario)
        if current_identity_id==id_usuario or current_identity_role.role=="admin":
            return usuario.to_json_admin()
        else:
            return usuario.to_json()
    #usuario.role=="admin" or usuario.id_usuario==id_usuario
    
    @role_required(roles=["admin"])
    def delete(self,id_usuario):
        usuario=db.session.query(UsuarioModel).get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'usuario eliminado correctamente', 204
    
    @jwt_required()
    def put(self,id_usuario):
        usuario = db.session.query(UsuarioModel).get_or_404(id_usuario)
        data = request.get_json().items()
        current_identity=get_jwt_identity()
        current_identity_role= db.session.query(UsuarioModel).filter_by(id_usuario=current_identity).first()
        current_identity_id = str(current_identity)
        id_usuario=str(id_usuario)
        if current_identity_id==id_usuario or current_identity_role.role=="admin":
            for key, value in data:
                setattr(usuario, key, value)
            db.session.add(usuario)
            db.session.commit()
            return usuario.to_json_complete() , 201
        else: return 'No se tienen permisos para editar'


class Usuarios(Resource):
    
    @role_required(roles=["admin"])
    def get(self):
        page=1
        per_page=10
        usuarios=db.session.query(UsuarioModel)
        if request.args.get('page'):
            page=int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page=int(request.args.get('per_page'))
        #revisar
        if request.args.get('MayorNroPrestamos'):
            usuarios=db.query(UsuarioModel,func.count(PrestamoModel.id_usuario).label('nro_prestamos')).outerjoin(PrestamoModel.usuario).group_by(UsuarioModel.id_usuario).order_by(func.count(PrestamoModel.id_usuario).desc().all())
            #usuarios=usuarios.outerjoin(UsuarioModel.prestamo).group_by(UsuarioModel.id_usuario).having(func.count(PrestamoModel.id_prestamo))
            return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios]})
        if request.args.get('activo'):
            usuarios=usuarios.filter(UsuarioModel.activo.like("%"+request.args.get('activo')+"%"))
        usuarios=usuarios.paginate(page=page,per_page=per_page,error_out=True)
        return jsonify({'usuarios': [usuario.to_json_admin() for usuario in usuarios],
                  'total': usuarios.total,
                  'pages': usuarios.pages,
                  'page': page
                })

    def post(self):
        usuario=UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201