from flask import Blueprint, request

util_routes = Blueprint("util_routes", __name__)


@util_routes.route("/", methods=["GET"])
def handle_request():
    if request.method == "GET":
        print("Running.")
        return "Running."

