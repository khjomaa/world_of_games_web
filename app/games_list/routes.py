from flask import render_template, url_for, flash,redirect, request, abort, Blueprint, session
from app.games_list.forms import PickGameForm

games = Blueprint('games_list', __name__)


@games.route('/gamepicker', methods=['GET', 'POST'])
def pick_game():
    player_name = session.get('player_name', None)

    form = PickGameForm()
    if request.method == 'POST':
        if form.play.data:
            if form.validate_on_submit():
                game = form.games.data
                session['difficulty'] = form.difficulty.data
                if game == '1':
                    session['random_numbers'] = []
                    return redirect(url_for('memory_game.play'))
                elif game == '2':
                    return redirect(url_for('guess_game.play'))
                elif game == '3':
                    return redirect(url_for('currency_roulette_game.play'))
            else:
                print(form.errors)
                flash('Please choose one of the games', 'danger')
                return redirect(url_for('games_list.pick_game'))
        elif form.save.data:
            return redirect(url_for('score_page.show'))

    return render_template('pick_game.html', title='Pick Game', form=form, name=player_name, score=session['score'])
