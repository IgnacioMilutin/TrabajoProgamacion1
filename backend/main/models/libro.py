from .. import db

class Libro(db.Model):
    id_libro=db.Column(db.Integer,primary_key=True)
    id_autor=db.Column(db.Integer, nullable=False)
    titulo=db.Column(db.String, nullable=False)
    genero=db.Column(db.String, nullable=False)
    editorial=db.Column(db.String, nullable=False)
    unidades=db.Column(db.Integer, nullable=False)
    estado=db.Column(db.Boolean, nullable=False)
    valoracion_total=db.Column(db.Float, nullable=False)

    def to_json(self):
        libro_json={
            'id_libro':int(self.id_libro),
            'id_autor':int(self.id_autor),
            'titulo':str(self.titulo),
            'genero':str(self.genero),
            'editorial':str(self.editorial),
            'unidades':int(self.unidades),
            'estado':(self.estado),
            'valoracion_total':(self.valoracion_total)
        }
        return libro_json
    
    def from_json(libro_json):
        id_libro=libro_json.get('id_libro')
        id_autor=libro_json.get('id_autor')
        titulo=libro_json.get('titulo')
        genero=libro_json.get('genero')
        editorial=libro_json.get('editorial')
        unidades=libro_json.get('unidades')
        estado=libro_json.get('estado')
        valoracion_total=libro_json.get('valoracion_total')
        return Libro(id_libro=id_libro,
                       id_autor=id_autor,
                       titulo=titulo,
                       genero=genero,
                       editorial=editorial,
                       unidades=unidades,
                       estado=estado,
                       valoracion_total=valoracion_total
                       )