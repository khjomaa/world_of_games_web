from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class CurrencyRouletteForm(FlaskForm):
    number = FloatField('Please guess the value of ', validators=[DataRequired(message='Only Integer and Decimal numbers are allowed')])
    submit = SubmitField("Check Result")
