from database import db


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


def update(player):
    sql = """
    UPDATE player
    SET nickname = :nickname,
    first_name = :first_name,
    last_name = :last_name,
    nick_first_last = :nick_first_last,
    hltv_id = :hltv_id
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


def get_player_by_property(table, property, value):
    try:
        sql = """
        SELECT * FROM :table WHERE :property = :value
        """
        result = db.session.execute(sql, {":property": value})
        print(result)
        item = result.fetchone()[0]
        return item
    except:
        return False


def get_all(table):
    try:
        print("in get_all")
        print(table)
        sql = """
            SELECT * FROM {} 
            """.format(
            table
        )
        result = db.session.execute(sql)
        items = result.fetchall()
        return items
    except:
        return False

