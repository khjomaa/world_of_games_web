from flask import render_template, url_for, flash, redirect, request, Blueprint, session

from app.memory_game.forms import MemoryForm
from app.utils import generate_random_numbers, add_score

memory = Blueprint('memory_game', __name__)


@memory.route('/memorygame', methods=['GET', 'POST'])
def play():
    form = MemoryForm()
    difficulty = int(session.get('difficulty', 1))

    if request.method == "GET":
        if not session['random_numbers']:
            session['random_numbers'] = generate_random_numbers(difficulty)
    elif request.method == "POST" and form.validate_on_submit():
        user_numbers = list(map(int, form.numbers.data.split(" ")))

        if set(session.get('random_numbers', [])) == set(user_numbers):
            add_score(difficulty)
            flash('Well Done!', 'success')
            return redirect(url_for('games_list.pick_game'))
        else:
            flash('You guessed wrong. Please try again', 'danger')
            form.numbers.data = ''

    return render_template('memory_game.html', title='Memory Game', form=form, numbers=session.get('random_numbers', []))
