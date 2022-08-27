from flask import Blueprint, request
from auth import require_auth

from controllers.player import update, get_all

player_routes = Blueprint("player_routes", __name__)


@player_routes.route("/player", methods=["GET", "POST"])
@require_auth
def handle_request():
    if request.method == "POST":
        print("in post player")
        data = request.get_json()
        print(data)
        update(data)
        return "Player inserted."
    if request.method == "GET":
        players = get_all("player")
        print("in get:")
        print(players)
        print(type(players))
        return "json.dumps(players)"

