from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Regexp


class GuessForm(FlaskForm):
    number = IntegerField('Please guess a number between 1 to', validators=[DataRequired(message='Only Integer numbers are allowed')])
    check_result = SubmitField("Check Result")
