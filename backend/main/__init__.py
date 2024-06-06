from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

api=Api()
db=SQLAlchemy()
#migrate.Migrate()
jwt=JWTManager()
mailsender=Mail()

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
    #.add_resource(resources.SigninResources,'/signin')
    #api.add_resource(resources.LoginResources,'/login/<nombre>/<contrasena>')
    api.add_resource(resources.PrestamoResources,'/prestamo/<id_prestamo>')
    api.add_resource(resources.PrestamosResources,'/prestamos')
    api.add_resource(resources.NotificacionResources,'/notificacion')
    api.add_resource(resources.ResenaResources,'/resena/<id_resena>')
    api.add_resource(resources.ResenasResources,'/resenas')
    api.add_resource(resources.AutorResources,'/autor/<id_autor>')
    api.add_resource(resources.AutoresResources,'/autores')
    api.init_app(app)

    app.config['JWT_SECRET_KEY']=os.getenv('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)
    from main.auth import routes
    app.register_blueprint(routes.auth)

    app.config['MAIL_HOSTNAME']=os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER']=os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT']=os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS']=os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME']=os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD']=os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER']=os.getenv('FLASKY_MAIL_SENDER')
    mailsender.init_app(app) 

    return app


