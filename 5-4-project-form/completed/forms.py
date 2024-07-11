from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

class HealthDataForm(FlaskForm):
    exercise = IntegerField('Exercise (minutes)')
    meditation = IntegerField('Meditation (minutes)')
    sleep = IntegerField('Sleep (hours)')
    submit = SubmitField('Submit')
