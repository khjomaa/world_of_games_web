from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    player_name = StringField(label='Please enter your name', validators=[DataRequired()])
    play = SubmitField(label="Let's Play")