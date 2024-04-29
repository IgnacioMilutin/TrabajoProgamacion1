from .. import db
import json

class Autor(db.Model):
    id_autor=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String,nullable=False)

    def to_json(self):
        autor_json={
            'id_autor':int(self.id_autor),
            'nombre':str(self.nombre),
        }
        return autor_json
    
    def from_json(autor_json):
        id_autor=autor_json.get('id_usuario')
        nombre=autor_json.get('nombre')
        return Autor(id_autor=id_autor,
                       nombre=nombre,
                       )
