from .. import db
from datetime import datetime
import json

#Tabla Relacion MM
libros_prestamos=db.Table("libros_pretamos",
    db.Column("id_libro",db.Integer,db.ForeignKey("libro.id_libro")),
    db.Column("id_prestamo",db.Integer,db.ForeignKey("prestamos.id_prestamo"))
    )

class Prestamos(db.Model):
    id_prestamo=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_inicio=db.Column(db.DateTime, nullable=False)
    fecha_limite=db.Column(db.DateTime, nullable=False)
    entrega=db.Column(db.String, nullable=False)
    #Relaciones
    usuario=db.relationship('Usuario',back_populates='prestamo')
    libros=db.relationship('Libro',secondary=libros_prestamos,backref=db.backref('prestamos',lazy='dynamic'))

    def to_json(self):
        prestamos_json={
            'id_prestamo':int(self.id_prestamo),
            'id_usuario':int(self.id_usuario),
            'fecha_inicio':str(self.fecha_inicio.strftime("%d-%m-%Y")),
            'fecha_limite':str(self.fecha_limite.strftime("%d-%m-%Y")),
            'entrega':str(self.entrega),
            'libro':[libro.to_json() for libro in self.libros]
        }
        return prestamos_json
    
    def from_json(prestamos_json):
        id_prestamo=prestamos_json.get('id_prestamo')
        id_usuario=prestamos_json.get('id_usuario')
        fecha_inicio=datetime.strptime(prestamos_json.get('fecha_inicio'),'%d-%m-%Y')
        fecha_limite=datetime.strptime(prestamos_json.get('fecha_limite'),'%d-%m-%Y')
        entrega=prestamos_json.get('entrega')
        return Prestamos(id_prestamo=id_prestamo,
                       id_usuario=id_usuario,
                       fecha_inicio=fecha_inicio,
                       fecha_limite=fecha_limite,
                       entrega=entrega
                       )
    
