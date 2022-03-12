from app import flask_app
from task_queue import add_scrape_to_queue


# @flask_app.route("/test")
# def testing():
#     print("here")
#     return "test"


@flask_app.route("/schedule-scrape/<resource>/<id>", methods=["POST"])
async def schedule_scrape(resource, id):
    print("in schedule-scrape route")
    print("resource: " + resource)
    print("id: " + id)
    await add_scrape_to_queue(resource, id)
    return "Success."


# def add_job(hltv_id):
#     scheduler.add_job(
#         id=str(uuid1()),
#         func=scrape_org,
#         trigger="date",
#         run_date=datetime.datetime.now() + datetime.timedelta(seconds=2),
#         jobstore="hltv_scraper",
#         executor="hltv_scraper",
#         args=[str(hltv_id)],
#     )
