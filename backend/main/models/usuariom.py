from .. import db
import json
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    nombreapellido=db.Column(db.String(100), nullable=False)
    mail=db.Column(db.String(100), nullable=False, unique=True, index=True)
    password=db.Column(db.String(100), nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    dni=db.Column(db.Integer, nullable=False)
    activo=db.Column(db.Boolean, nullable=False)
    role=db.Column(db.String(10),nullable=False, server_default="user")

    resena=db.relationship('Resenas',back_populates='usuario',cascade="all, delete-orphan")
    prestamo=db.relationship('Prestamos',back_populates='usuario',cascade="all, delete-orphan")
    notificacion=db.relationship('Notificacion',back_populates='usuario',cascade="all, delete-orphan")

    @property
    def plain_password(self):
        raise AttributeError("Password cant be read")
    
    @plain_password.setter
    def plain_password(self, password):
        self.password=generate_password_hash(password)
        
    def validate_pass(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombreapellido))

    def to_json(self):
        usuario_json={
            'id_usuario':(self.id_usuario),
            'nombreapellido':(self.nombreapellido),
            'mail':(self.mail),
        }
        return usuario_json
    
    def to_json_complete(self):
        notificacion=[notificacion.to_json() for notificacion in self.notificacion]
        usuario_json={
            'id_usuario':(self.id_usuario),
            'nombreapellido':(self.nombreapellido),
            'mail':(self.mail),
            'password':(self.password),
            'telefono':(self.telefono),
            'dni':(self.dni),
            'activo':self.activo
        }
        return usuario_json
    
    def to_json_admin(self):
        notificacion=[notificacion.to_json() for notificacion in self.notificacion]
        usuario_json={
            'id_usuario':(self.id_usuario),
            'nombreapellido':(self.nombreapellido),
            'mail':(self.mail),
            'password':(self.password),
            'telefono':(self.telefono),
            'dni':(self.dni),
            'activo':self.activo,
            'role':self.role
        }
        return usuario_json
    
    def from_json(usuario_json):
        id_usuario=usuario_json.get('id_usuario')
        nombreapellido=usuario_json.get('nombreapellido')
        mail=usuario_json.get('mail')
        password=usuario_json.get('password')
        telefono=usuario_json.get('telefono')
        dni=usuario_json.get('dni')
        activo=usuario_json.get('activo')
        role=usuario_json.get('role')
        return Usuario(id_usuario=id_usuario,
                       nombreapellido=nombreapellido,
                       mail=mail,
                       plain_password=password,
                       telefono=telefono,
                       dni=dni,
                       activo=activo,
                       role=role
                       )
