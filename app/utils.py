import random
import requests
from flask import session

from app import db
from app.models import Scores

BASE_URL = 'https://api.exchangerate-api.com/v4/latest/USD'


def generate_random_number(difficulty):
    rand_num = random.randint(1, difficulty)
    return rand_num


def generate_random_numbers(difficulty):
    random_numbers = []

    for i in range(difficulty):
        random_numbers.append(random.randint(1, difficulty))

    return random_numbers


def get_money_interval(difficulty):
    response = requests.get(BASE_URL)
    data = response.json()
    ils_rate = data['rates']['ILS']
    total_value = difficulty * ils_rate
    return round(total_value - (5 - difficulty), 2), round(total_value + (5 - difficulty), 2)


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    if 'score' not in session:
        session['score'] = 0

    session['score'] = session['score'] + points_of_winning
    print(session['score'])


def save_score_to_db(player_name, score):
    player = Scores.query.filter_by(player_name=player_name).first()
    if not player:
        player = Scores(player_name, score)
        db.session.add(player)
        db.session.commit()
    else:
        player.score += score
        db.session.commit()
