from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class HealthDataForm(FlaskForm):
    exercise = IntegerField('Exercise (minutes)', validators=[InputRequired(), NumberRange(min=0)])
    meditation = IntegerField('Meditation (minutes)', validators=[InputRequired(), NumberRange(min=0)])
    sleep = IntegerField('Sleep (hours)', validators=[InputRequired(), NumberRange(min=0, max=24)])
    submit = SubmitField('Submit')
