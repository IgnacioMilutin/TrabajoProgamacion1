from .. import db

class Usuario(db.Model):
    id_usuario=db.Column(db.Integer,primary_key=True)
    nombreapellido=db.Column(db.String(100), nullable=False)
    correo=db.Column(db.String(100), nullable=False)
    contrasena=db.Column(db.String(100), nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    dni=db.Column(db.Integer, nullable=False)
    estado=db.Column(db.Boolean, nullable=False)

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
            'estado':self.estado
        }
        return usuario_json
    
    def from_json(usuario_json):
        id_usuario=usuario_json.get('id_usuario')
        nombreapellido=usuario_json.get('nombreapellido')
        correo=usuario_json.get('correo')
        contrasena=usuario_json.get('contrasena')
        telefono=usuario_json.get('telefono')
        dni=usuario_json.get('dni')
        estado=usuario_json.get('estado')
        return Usuario(id_usuario=id_usuario,
                       nombreapellido=nombreapellido,
                       correo=correo,
                       contrasena=contrasena,
                       telefono=telefono,
                       dni=dni,
                       estado=estado
                       )
