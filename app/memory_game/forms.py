from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp


class MemoryForm(FlaskForm):
    numbers = StringField('Please enter the numbers separated with space',
                          validators=[DataRequired(),
                                      Regexp('^[0-9 ]*$', message='Only 0-9 numbers are allowed')])
    submit = SubmitField("Check Result")
