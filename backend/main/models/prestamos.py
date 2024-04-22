from .. import db

class Prestamos(db.Model):
    id_prestamo=db.Column(db.Integer,primary_key=True)
    id_libro=db.Column(db.Integer, nullable=False)
    id_usuario=db.Column(db.Integer, nullable=False)
    fecha_inicio=db.Column(db.DateTime, nullable=False)
    fecha_limite=db.Column(db.DateTime, nullable=False)

    def to_json(self):
        prestamos_json={
            'id_prestamo':int(self.id_prestamo),
            'id_libro':int(self.id_libro),
            'id_usuario':int(self.id_usuario),
            'fecha_inicio':(self.fecha_inicio),
            'fecha_limite':(self.fecha_limite),
        }
        return prestamos_json
    
    def from_json(prestamos_json):
        id_prestamo=prestamos_json.get('id_prestamo')
        id_libro=prestamos_json.get('id_libro')
        id_usuario=prestamos_json.get('id_usuario')
        fecha_inicio=prestamos_json.get('fecha_inicio')
        fecha_limite=prestamos_json.get('fecha_limite')
        return Prestamos(id_prestamo=id_prestamo,
                       id_libro=id_libro,
                       id_usuario=id_usuario,
                       fecha_inicio=fecha_inicio,
                       fecha_limite=fecha_limite,
                       )