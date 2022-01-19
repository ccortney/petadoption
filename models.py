"""Models for Pet Adoption Application"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """connect this database to provided Flask app"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, default = True, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLNcJf23tDgKUIl-zbnfx-5pSIj50UVgreg&usqp=CAU")

