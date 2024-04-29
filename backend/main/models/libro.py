from .. import db
import json

#Tabla Relacion MM
libros_autores=db.Table("libros_autores",
    db.Column("id_libro",db.Integer,db.ForeignKey("libro.id_libro")),
    db.Column("id_autor",db.Integer,db.ForeignKey("autor.id_autor"))
    )

class Libro(db.Model):
    id_libro=db.Column(db.Integer,primary_key=True)
    titulo=db.Column(db.String, nullable=False)
    genero=db.Column(db.String, nullable=False)
    editorial=db.Column(db.String, nullable=False)
    unidades=db.Column(db.Integer, nullable=False)
    activo=db.Column(db.Boolean, nullable=False)
    valoracion_total=db.Column(db.Float, nullable=False)
    #Relaciones
    resena=db.relationship('Resenas',back_populates='libro',cascade="all, delete-orphan")
    autores=db.relationship('Autor',secondary=libros_autores, backref=db.backref('libros',lazy='dynamic'))
    
    def to_json(self):
        libro_json={
            'id_libro':int(self.id_libro),
            'titulo':str(self.titulo),
            'genero':str(self.genero),
            'editorial':str(self.editorial),
            'unidades':int(self.unidades),
            'activo':(self.activo),
            'valoracion_total':(self.valoracion_total),
            'autores':[autor.to_json() for autor in self.autores]
        }
        return libro_json
    
    def from_json(libro_json):
        id_libro=libro_json.get('id_libro')
        titulo=libro_json.get('titulo')
        genero=libro_json.get('genero')
        editorial=libro_json.get('editorial')
        unidades=libro_json.get('unidades')
        activo=libro_json.get('activo')
        valoracion_total=libro_json.get('valoracion_total')
        return Libro(id_libro=id_libro,
                       titulo=titulo,
                       genero=genero,
                       editorial=editorial,
                       unidades=unidades,
                       activo=activo,
                       valoracion_total=valoracion_total
                       )