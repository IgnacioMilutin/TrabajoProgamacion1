from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy


api=Api()
db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    load_dotenv()

#BASE DE DATOS
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    
#RECURSOS
    import main.resources as resources    
    api.add_resource(resources.UsuariosResources,'/usuarios')
    api.add_resource(resources.UsuarioResources,'/usuario/<id_usuario>')
    api.add_resource(resources.LibrosResources,'/libros')
    api.add_resource(resources.LibroResources,'/libro/<id_libro>')
    api.add_resource(resources.SigninResources,'/signin')
    #api.add_resource(resources.LoginResources,'/login/<nombre>/<contrasena>')
    api.add_resource(resources.PrestamoResources,'/prestamo/<id_prestamo>')
    api.add_resource(resources.PrestamosResources,'/prestamos')
    api.add_resource(resources.Prestamos_por_usuarioResources,'/prestamos_usuario/<id_usuario>')
    api.add_resource(resources.Prestamos_por_libroResources,'/prestamos_libro/<id_libro>')
    api.add_resource(resources.NotificacionResources,'/notificacion')
    api.add_resource(resources.Notificacion_por_usuarioResources,'/notificacion_usuario/<id_usuario>')
    api.add_resource(resources.ResenaResources,'/resena/<id_resena>')
    api.add_resource(resources.ResenasResources,'/resenas')
    api.add_resource(resources.Resenas_por_usuarioResources,'/resenas_usuario/<id_usuario>')
    api.add_resource(resources.Resenas_por_libroResources,'/resenas_libro/<id_libro>')
    api.add_resource(resources.AutorResources,'/autor/<id_autor>')
    api.add_resource(resources.AutoresResources,'/autores')
    api.init_app(app)
    return app
