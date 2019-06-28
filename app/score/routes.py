from flask import render_template, url_for, redirect, Blueprint, session, request

from app.utils import save_score_to_db

score_page = Blueprint('score_page', __name__)


@score_page.route('/savegame', methods=['GET', 'POST'])
def show():

    if request.method == "POST":
        if request.form['submit_button'] == 'save_and_quit':
            player_name = session['player_name']
            score = session['score']
            if score != 0:
                save_score_to_db(player_name, score)
            session.clear()
            return redirect(url_for('main.index'))
        elif request.form['submit_button'] == 'back_to_games':
            return redirect(url_for('games_list.pick_game'))
    elif request.method == "GET":
        if 'player_name' not in session and 'score' not in session:
            return redirect(url_for('main.index'))

    return render_template('score.html', title='Save Game', player_name=session['player_name'], score=session['score'])
