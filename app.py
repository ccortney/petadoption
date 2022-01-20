"""Pet Adoption Application."""

from ast import Add
from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import PetForm


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

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add pet form, handles adding a pet when submitted"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        available = form.availibility.data
        notes = form.notes.data
        image_url = form.image_url.data
        
        new_pet = Pet(name = name, species = species, age = age, available = available, notes = notes, 
            image_url = image_url)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template("add_pet_form.html", form = form)

@app.route('/pet/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet form, handles adding a pet when submitted"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.available = form.availibility.data
        pet.notes = form.notes.data
        pet.image_url = form.image_url.data
        
        db.session.commit()
        return redirect(f'/pet/{pet_id}')
    
    else:
        return render_template("edit_pet_form.html", form = form, pet = pet)

@app.route('/pet/<int:pet_id>/delete')
def delete_pet(pet_id):
    """Delete"""

    pet = Pet.query.filter_by(id = pet_id)
    pet.delete()
    db.session.commit()

    return redirect('/')
