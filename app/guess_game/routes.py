from flask import render_template, url_for, flash,redirect, request, Blueprint, session

from app.guess_game.forms import GuessForm
from app.utils import generate_random_number, add_score

guess = Blueprint('guess_game', __name__)


@guess.route('/guessgame', methods=['GET', 'POST'])
def play():
    form = GuessForm()
    difficulty = int(session.get('difficulty', 1))

    if request.method == "GET":
        session['random_number'] = generate_random_number(difficulty)
    elif request.method == "POST" and form.validate_on_submit():
        user_guess = int(form.number.data)

        if user_guess == session['random_number']:
            add_score(difficulty)
            flash('Well Done!', 'success')
            return redirect(url_for('games_list.pick_game'))
        else:
            flash('You guessed wrong. Please try again', 'danger')
            form.number.data = ''

    return render_template('guess_game.html', title='Guess Game', form=form, difficulty=difficulty)
