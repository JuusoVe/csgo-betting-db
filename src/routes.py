from src.app import app
from src.services.hltv_scraper import scrape_player, scrape_team


@app.route("/")
def index():
    return 'index'


@app.route("/scrape/player/<hltv_id>")
def handle_scrape_player(hltv_id):
    player = scrape_player(hltv_id)
    return player


@app.route("/scrape/team/<hltv_id>")
def handle_scrape_team(hltv_id):
    team = scrape_team(hltv_id)
    print(team)
    return team
