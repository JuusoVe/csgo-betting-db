def parse_real_name(name):
    stripped_name = name.strip()
    name_list = stripped_name.split(" ")
    if len(name_list) == 1:
        return name_list.insert(1, '')
    if len(name_list) == 2:
        return name_list
    return [name_list[0], name_list[-1]]


def parse_nickname(nickname):
    stripped_nickname = nickname.strip()
    return stripped_nickname


def parse_player_from_image_title(title):
    title.strip()
    title_list = title.split(" ")
    player = {
        "first_name": title_list[0],
        "last_name": title_list[2],
        "nickname": title_list[1].strip("'"),
    }
    nick_first_last = parse_nick_first_last(player)
    player["nick_first_last"] = nick_first_last
    return player


def parse_nick_first_last(player):
    return player["nickname"].lower() + player["first_name"].lower() + player["last_name"].lower()


def parse_hltv_id_from_url(url):
    id_slash_nick = url[8:]
    hltv_id = id_slash_nick[0:id_slash_nick.find('/')]
    return hltv_id


def format_for_db(string):
    return string.isalnum().lower()


def parse_coach_form_link_element(elements):
    first_name_element = elements[1]
    first_name = str(first_name_element).strip().lower()
    last_name_element = elements[3]
    last_name = str(last_name_element).strip().lower()
    nickname_element = elements[2]
    nickname_string = str(nickname_element)
    nickname = nickname_string.split("'")[1]
    coach = {
        "first_name": first_name,
        "last_name": last_name,
        "nickname": nickname
    }
    return coach
