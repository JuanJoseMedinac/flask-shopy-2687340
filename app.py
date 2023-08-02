#dependencia de flask
from flask import Flask

#depndencia de los modelos 
from flask_sqlalchemy import SQLAlchemy

#depededncia de migraciones 
from flask_migrate import Migrate

#dependencia para fecha y hora 
from datetime import datetime

#crear el objeto flask
app = Flask(__name__)

#definifr la 'cadena de conexion'(conectionString)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/flask_shopy_2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#crear el objeto de modelos
db = SQLAlchemy(app)

#crear el objeto de migracion
migrate = Migrate(app, db)

#crear los modelos:
class cliente(db.Model):
    #definir los atributos
    __tablename__= "clientes"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(120), nullable = True)
    email = db.Column(db.String(120), nullable = True)

class producto (db.Model):
    #definir los atributos
    __tablename__= "productos"
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    precio = db.Column(db.Numeric(precision=10, scale=2), nullable = True)
    imagen = db.Column(db.String(200), nullable = True)

class venta (db.Model):
    #definir los atributos
    __tablename__= "ventas"
    id = db.Column(db.Integer,primary_key = True)
    fecha = db.Column (db.DateTime,default=datetime.utcnow )
    #calve foranea
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class detalle (db.Model):
    #definir los atributos
    __tablename__= "detalles"
    id = db.Column(db.Integer,primary_key = True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)