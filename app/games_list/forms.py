from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectField


class PickGameForm(FlaskForm):
    games = RadioField(
        label='Please choose a game to play:',
        choices=[
            ('1', 'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'),
            ('2', 'Guess Game - guess a number and see if you chose like the computer'),
            ('3', 'Currency Roulette - try and guess the value of a random amount of USD in ILs')
        ]
    )

    difficulty = SelectField(
        label='Choose difficulty:',
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    )

    play = SubmitField(label='Play')
    save = SubmitField(label='My Score')

