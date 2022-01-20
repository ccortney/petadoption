from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class PetForm(FlaskForm):
    """Form for adding Pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices = [("Dog", "Dog"), ("Cat", "Cat"), ("Bunny", "Bunny")],
        validators=[InputRequired()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Invalid length')])
    notes = StringField("Notes", validators=[Optional()])
    availibility = BooleanField("Check if Currently Available for Adoption")
    image_url = StringField("Image Url", validators =[URL(), Optional()])
