from .. import db
import json
from datetime import datetime

#usuario_notificacion=db.Table("usuario_notificacion",
#    db.Column("id_usuario",db.Integer,db.ForeignKey("usuario.id_usuario")),
#    db.Column("id_notificacion",db.Integer,db.ForeignKey("notificacion.id_notificacion"))
#    )

class Notificacion(db.Model):
    id_notificacion=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id_usuario"), nullable=False)
    fecha=db.Column(db.DateTime, nullable=False)
    entrega=db.Column(db.Boolean, nullable=False)
    comentario=db.Column(db.String, nullable=False)
    #Relaciones
    #usuarios=db.relationship('Usuario',secondary=usuario_notificacion,backref=db.backref('notificacion',lazy='dynamic'))
    usuario=db.relationship('Usuario',back_populates='notificacion')

    def to_json(self):
        notificacion_json={
            'id_notificacion':int(self.id_notificacion),
            'id_usuario':int(self.id_usuario),
            'fecha':str(self.fecha.strftime("%d-%m-%Y %H:%M")),
            'entrega':(self.entrega),
            'comentario':str(self.comentario)
        }
        return notificacion_json
    
    def to_json_complete(self):
        usuario=[usuario.to_json() for usuario in self.usuario]
        notificacion_json={
            'id_prestamo':int(self.id_notificacion),
            'id_usuario':int(self.id_usuario),
            'fecha':str(self.fecha.strftime("%d-%m-%Y %H:%M")),
            'entrega':(self.entrega),
            'comentario':str(self.comentario),
            'usuarios':[usuario.to_json() for usuario in self.usuario]
        }
        return notificacion_json

    def from_json(notificacion_json):
        id_notificacion=notificacion_json.get('id_notificacion')
        id_usuario=notificacion_json.get('id_usuario')
        fecha=datetime.strptime(notificacion_json.get('fecha'),'%d-%m-%Y %H:%M')
        entrega=notificacion_json.get('entrega')
        comentario=notificacion_json.get('comentario')
        return Notificacion(id_notificacion=id_notificacion,
                        id_usuario=id_usuario,
                        fecha=fecha,
                        entrega=entrega,
                        comentario=comentario
                       )