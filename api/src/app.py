from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.player import player_routes

app = Flask(__name__)

app.register_blueprint(player_routes)


@app.route("/health")
def testing():
    print("App is running.")
    return "App is running."


flask_config = getenv("ENV_SETTINGS", "config.FlaskDevelopmentConfig")
app.config.from_object(flask_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    print("Running flask app.")
