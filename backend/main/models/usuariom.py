from .. import db
import json

class Usuario(db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    nombreapellido=db.Column(db.String(100), nullable=False)
    correo=db.Column(db.String(100), nullable=False)
    contrasena=db.Column(db.String(100), nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    dni=db.Column(db.Integer, nullable=False)
    activo=db.Column(db.Boolean, nullable=False)
    #Relaciones
    notificacion=db.relationship('Notificacion',back_populates='usuario',cascade="all, delete-orphan")
    resena=db.relationship('Resenas',back_populates='usuario',cascade="all, delete-orphan")
    prestamo=db.relationship('Prestamos',back_populates='usuario',cascade="all, delete-orphan")

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombreapellido))

    def to_json(self):
        usuario_json={
            'id_usuario':(self.id_usuario),
            'nombreapellido':(self.nombreapellido),
            'correo':(self.correo),
            'contrasena':(self.contrasena),
            'telefono':(self.telefono),
            'dni':(self.dni),
            'activo':self.activo
        }
        return usuario_json
    
    def to_json_complete(self):
        notificacion=[notificacion.to_json() for notificacion in self.notificacion]
        usuario_json={
            'id_usuario':(self.id_usuario),
            'nombreapellido':(self.nombreapellido),
            'correo':(self.correo),
            'contrasena':(self.contrasena),
            'telefono':(self.telefono),
            'dni':(self.dni),
            'activo':self.activo
        }
        return usuario_json
    
    def from_json(usuario_json):
        id_usuario=usuario_json.get('id_usuario')
        nombreapellido=usuario_json.get('nombreapellido')
        correo=usuario_json.get('correo')
        contrasena=usuario_json.get('contrasena')
        telefono=usuario_json.get('telefono')
        dni=usuario_json.get('dni')
        activo=usuario_json.get('activo')
        return Usuario(id_usuario=id_usuario,
                       nombreapellido=nombreapellido,
                       correo=correo,
                       contrasena=contrasena,
                       telefono=telefono,
                       dni=dni,
                       activo=activo
                       )
