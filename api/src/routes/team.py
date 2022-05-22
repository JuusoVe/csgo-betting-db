from flask import request
from app import app





@app.route("/team", methods=["POST"])
def schedule_scrape(resource, id):
    print("in schedule-scrape route")
    print("resource: " + resource)
    print("id: " + id)
    return "Success."

