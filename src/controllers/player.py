from src.app import create_app
from src.models import db

app = create_app()
app.app_context().push()


def add_new(player):
    try:
        sql = "INSERT INTO player (nickname, first_name, last_name, nick_first_last, hltv_id) VALUES (:nickname, :first_name, :last_name, :nick_first_last, :hltv_id)"
        db.session.execute(sql, player)
        db.session.commit()

    except Exception as e:
        return False
    return True
