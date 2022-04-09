from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_config = getenv("ENV_SETTINGS", "config.FlaskDevelopmentConfig")
app = Flask(__name__)
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
