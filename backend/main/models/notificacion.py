from .. import db
import json

class Notificacion(db.Model):
    id_notificacion=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id_usuario"), nullable=False)
    entregado=db.Column(db.Boolean, nullable=False)
    comentario=db.Column(db.String, nullable=False)
    #Relaciones
    usuario=db.relationship('Usuario',back_populates='notificacion')


    def to_json(self):
        notificacion_json={
            'id_prestamo':int(self.id_notificacion),
            'id_usuario':int(self.id_usuario),
            'entregado':(self.entregado),
            'comentario':str(self.comentario),
        }
        return notificacion_json
    
    def to_json_complete(self):
        usuario=[usuario.to_json() for usuario in self.usuario]
        notificacion_json={
            'id_prestamo':int(self.id_notificacion),
            'id_usuario':int(self.id_usuario),
            'entregado':(self.entregado),
            'comentario':str(self.comentario),
            'usuario':usuario
        }
        return notificacion_json

    def from_json(notificacion_json):
        id_notificacion=notificacion_json.get('id_notificacion')
        id_usuario=notificacion_json.get('id_usuario')
        entregado=notificacion_json.get('entregado')
        comentario=notificacion_json.get('comentario')
        return Notificacion(id_notificacion=id_notificacion,
                       id_usuario=id_usuario,
                       entregado=entregado,
                       comentario=comentario
                       )