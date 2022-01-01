import os
from flask import Flask
from flask import redirect, render_template, request
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
env_config = os.getenv("ENV_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    # result = db.session.execute("SELECT COUNT(*) FROM messages")
    # count = result.fetchone()[0]
    # result = db.session.execute("SELECT content FROM messages")
    # messages = result.fetchall()
    # return render_template("index.html", content=os.getenv("APP_SETTINGS")
    return  os.getenv("DATABASE_URI")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")