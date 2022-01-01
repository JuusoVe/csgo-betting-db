from app import app
from flask import redirect, render_template, request

@app.route("/")
def index():
    return 'index'

@app.route("/scrape/player/<hltvid>")
def scrapeplayer(hltvid):
    return hltvid

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")