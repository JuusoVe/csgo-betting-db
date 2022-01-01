from app import app
from flask import redirect, render_template, request
from scrapers import scrape_player


@app.route("/")
def index():
    return 'index'
    # https://realpython.com/beautiful-soup-web-scraper-python/#step-1-inspect-your-data-source

@app.route("/scrape/player/<hltv_id>")
def handle_scrape_player(hltv_id):
    player = scrape_player(hltv_id)
    return player

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")