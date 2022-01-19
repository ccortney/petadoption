"""Pet Adoption Application."""

from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'pets'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template("homepage.html", pets = pets)

@app.route('/pet/<int:pet_id>')
def pet_details(pet_id):
    pet = Pet.query.get(pet_id)

    return render_template("pet_details.html", pet = pet)


