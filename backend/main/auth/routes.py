from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from main.mail.function import sendMail

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login',methods=['POST'])
def login():
    usuario=db.session.query(UsuarioModel).filter(UsuarioModel.mail==request.get_json().get("mail")).first_or_404()
    if usuario.validate_pass(request.get_json().get("password")):
        access_token=create_access_token(identity=usuario)
        data={
            'id_usuario':(usuario.id_usuario),
            'mail':usuario.mail,
            'access_token':access_token
        }
        return data,200
    else: return 'Incorrect password', 401

@auth.route('/signin', methods=['POST'])
def signin():
    usuario=UsuarioModel.from_json(request.get_json())
    exists=db.session.query(UsuarioModel).filter(UsuarioModel.mail==usuario.mail).scalar() is not None
    if exists:
        return 'Duplicated mail', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
            send=sendMail([usuario.mail],"Welcome!","signin",usuario=usuario)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(), 201