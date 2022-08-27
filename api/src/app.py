from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
from routes.player import player_routes
from routes.util import util_routes


def create_app():
    app = Flask(__name__)
    flask_config = getenv("ENV_SETTINGS", "config.FlaskDevelopmentConfig")
    app.config.from_object(flask_config)
    db.init_app(app)
    app.register_blueprint(util_routes)
    app.register_blueprint(player_routes)
    return app


def setup_database(app):
    with app.app_context():
        db.init_app(app)


def migrate(app, db):
    Migrate(app, db)


if __name__ == "__main__":
    app = create_app()
    setup_database(app)
    migrate(app, db)
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Running flask app.")
