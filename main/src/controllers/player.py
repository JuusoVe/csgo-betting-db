from src.models import db


def add_new(player):
    sql = """
    INSERT INTO player
    (nickname, first_name, last_name, nick_first_last, hltv_id)
    VALUES
    (:nickname, :first_name, :last_name, :nick_first_last, :hltv_id)
    """
    db.session.execute(sql, player)
    db.session.commit()
    return True


def get_id_for_nick_first_last(nick_first_last):
    try:
        sql = """
        SELECT id FROM player WHERE nick_first_last = :nick_first_last
        """
        result = db.session.execute(sql, {"nick_first_last": nick_first_last})
        print(result)
        player_id = result.fetchone()[0]
        return player_id
    except:
        return False
