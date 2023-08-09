#dependencia de flask
from flask import Flask, render_template

#depndencia de los modelos 
from flask_sqlalchemy import SQLAlchemy

#depededncia de migraciones 
from flask_migrate import Migrate

#dependencia para fecha y hora 
from datetime import datetime
#dependencias de wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#crear el objeto flask
app = Flask(__name__)

#definifr la 'cadena de conexion'(conectionString)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/flask_shopy_2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY']='2687340'

#crear el objeto de modelos
db = SQLAlchemy(app)

#crear el objeto de migracion
migrate = Migrate(app, db)

#crear formulario de registro de productos 
class ProductosForm(FlaskForm):
    nombre = StringField ('nombre_producto')
    nprecio = StringField ('precio_producto')
    submit = SubmitField('registrar producto')


#crear los modelos:
class cliente(db.Model):
    #definir los atributos
    __tablename__= "clientes"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120), nullable = True)
    password = db.Column(db.String(120), nullable = True)
    email = db.Column(db.String(120), nullable = True)

    #relaciones sql alchemy
    ventas=db.relationship('venta', 
                           backref="cliente", 
                           lazy ="dynamic")


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

    #rutas:
@app.route('/producto', methods =['GET', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    #nuevo producto
    if form.validate_on_submit():
        p3=producto (nombre = form.nombre.data , precio=form.nprecio.data )
        db.session.add(p3)
        db.session.commit()
        return "producto registrado"
    return render_template('nuevo_producto.html', 
                           form = form)
    
