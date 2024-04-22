from .. import db

class Notificacion(db.Model):
    id_notificacion=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer, nullable=False)
    estado=db.Column(db.Boolean, nullable=False)
    comentario=db.Column(db.String, nullable=False)

    def to_json(self):
        notificacion_json={
            'id_prestamo':int(self.id_notificacion),
            'id_usuario':int(self.id_usuario),
            'estado':(self.estado),
            'comentario':str(self.comentario),
        }
        return notificacion_json
    
    def from_json(notificacion_json):
        id_notificacion=notificacion_json.get('id_notificacion')
        id_usuario=notificacion_json.get('id_usuario')
        estado=notificacion_json.get('estado')
        comentario=notificacion_json.get('comentario')
        return Notificacion(id_notificacion=id_notificacion,
                       id_usuario=id_usuario,
                       estado=estado,
                       comentario=comentario
                       )