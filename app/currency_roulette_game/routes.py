from flask import render_template, url_for, flash,redirect, request, Blueprint, session

from app.currency_roulette_game.forms import CurrencyRouletteForm
from app.utils import get_money_interval, add_score

currency_roulette = Blueprint('currency_roulette_game', __name__)


@currency_roulette.route('/currency_roulette_game', methods=['GET', 'POST'])
def play():
    form = CurrencyRouletteForm()
    difficulty = int(session.get('difficulty', 1))

    if request.method == "GET":
        session['usd_rate'] = get_money_interval(difficulty)
    elif request.method == "POST" and form.validate_on_submit():
        user_guess = float(form.number.data)
        lower, higher = session['usd_rate']

        if lower <= user_guess <= higher:
            add_score(difficulty)
            flash('Well Done!', 'success')
            return redirect(url_for('games_list.pick_game'))
        else:
            flash('You guessed wrong. Please try again', 'danger')
            form.number.data = ''

    return render_template('currency_roulette_game.html', title='Currency Roulette Game', form=form, difficulty=difficulty)
