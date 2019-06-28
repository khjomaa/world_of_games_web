from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # load config
    app.config.from_object((set_environment_config()))

    # Initialize db
    db.init_app(app)

    # import blueprints and register them
    from app.main.routes import main
    app.register_blueprint(main)

    from app.games_list.routes import games
    app.register_blueprint(games)

    from app.memory_game.routes import memory
    app.register_blueprint(memory)

    from app.guess_game.routes import guess
    app.register_blueprint(guess)

    from app.currency_roulette_game.routes import currency_roulette
    app.register_blueprint(currency_roulette)

    from app.score.routes import score_page
    app.register_blueprint(score_page)

    from app.errors.handlers import errors
    app.register_blueprint(errors)

    # import models
    from app import models

    return app


def set_environment_config():
    if Config.ENV == "PRODUCTION":
        return 'config.ProductionConfig'
    elif Config.ENV == "DEVELOPMENT":
        return 'config.DevelopmentConfig'
