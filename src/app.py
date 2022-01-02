import os
from flask import Flask
from flask_migrate import Migrate
from src.models import db
import src.services.scheduler


def create_app():
    app = Flask(__name__)
    env_config = os.getenv("ENV_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object("src." + env_config)
    db.init_app(app)
    return app


migrate = Migrate(create_app(), db)


# from routes import *
