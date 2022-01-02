import os
from flask import Flask

from flask_migrate import Migrate
from models import Player, db

app = Flask(__name__)
env_config = os.getenv("ENV_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
db.init_app(app)
migrate = Migrate(app, db)

import src.routes as routes

