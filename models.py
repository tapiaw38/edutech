from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
import datetime
db = SQLAlchemy()

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    email = db.Column(db.String(40), nullable=True)
    tel = db.Column(db.String(8))
    comentario = db.Column(db.String(200))
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
