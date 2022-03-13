def parse_player_from_image_title_to_player_dict(title):
    """
    Parsing function to extract a player object from a image title on hltv team page

    Parameters:
      title (str): Image title string from hltv ie. "Aleksandr 's1mple' Kostyliev"

    Returns:
      player (dict): Object with the name parts parsed into properties.
    """
    title.strip()
    title_list = title.split(" ")
    player = {
        "first_name": title_list[0],
        "last_name": title_list[2],
        "nickname": title_list[1].strip("'"),
    }
    player["nick_first_last"] = parse_nick_first_last(player)
    return player


def parse_player_dict_to_nickfirstlast(player):
    """
    Parsing function to parse a player object with nickname, first_name and last_name
    into a nickfirstlast to be used as a pseudo-unique identifier.

    Parameters:
      player (dict): 

    Returns:
      nickfirstlast (str): Concat of nickname, first_name and last_name in lower case.
    """
    return player["nickname"].lower() + player["first_name"].lower() + player["last_name"].lower()