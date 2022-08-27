import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_config = os.getenv("ENV_SETTINGS", "config.FlaskDevelopmentConfig")
flask_app.config.from_object(flask_config)

db = SQLAlchemy(flask_app)

migrate = Migrate(flask_app, db)

import routes
