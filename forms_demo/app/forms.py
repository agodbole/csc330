from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PopulationForm(FlaskForm):
    city = StringField('City:', validators=[DataRequired()])
    population = IntegerField('Population: ', validators=[DataRequired()])
    submit = SubmitField('Save')
