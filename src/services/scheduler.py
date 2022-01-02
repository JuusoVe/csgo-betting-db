from src.services.hltv_scraper import scrape_team_players
from src.controllers.player import add_new

team = scrape_team_players("4608")

for player in team:
    add_new(player)
