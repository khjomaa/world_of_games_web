from app import db


class Scores(db.Model):

    __tablename__ = 'users_scores'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    def __repr__(self):
        return f'Scores: Player name: {self.player_name}, Score: {self.score}'
