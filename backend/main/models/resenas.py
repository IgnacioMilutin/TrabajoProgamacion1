from .. import db

class Resenas(db.Model):
    id_resena=db.Column(db.Integer,primary_key=True)
    id_libro=db.Column(db.Integer,db.ForeignKey("libro.id_libro"), nullable=False)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id_usuario"), nullable=False)
    valoracion=db.Column(db.Float, nullable=False)
    comentario=db.Column(db.String, nullable=True)
    #Relaciones
    usuario=db.relationship('Usuario',back_populates='resena')
    libro=db.relationship('Libro',back_populates='resena')

    def to_json(self):
        resenas_json={
            'id_resena':int(self.id_resena),
            'id_libro':int(self.id_libro),
            'id_usuario':int(self.id_usuario),
            'valoracion':(self.valoracion),
            'comentario':str(self.comentario),
        }
        return resenas_json
    
    def from_json(resenas_json):
        id_resena=resenas_json.get('id_resena')
        id_libro=resenas_json.get('id_libro')
        id_usuario=resenas_json.get('id_usuario')
        valoracion=resenas_json.get('valoracion')
        comentario=resenas_json.get('comentario')
        return Resenas(id_resena=id_resena,
                       id_libro=id_libro,
                       id_usuario=id_usuario,
                       valoracion=valoracion,
                       comentario=comentario,
                       )