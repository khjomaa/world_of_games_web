from flask import render_template, url_for, redirect, request, Blueprint, session

from app.main.forms import MainForm

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    form = MainForm()
    if request.method == 'POST' and form.validate_on_submit():
        session['player_name'] = form.player_name.data
        session['score'] = 0
        print(session['player_name'])
        return redirect(url_for('games_list.pick_game'))

    return render_template('home.html', form=form)
