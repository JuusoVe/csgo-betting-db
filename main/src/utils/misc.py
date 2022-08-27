from src.utils.parsers import parse_nick_first_last


def add_nick_first_last_and_sort(players_list):
    for player in players_list:
        player["nick_first_last"] = parse_nick_first_last(player)
    sorted_list = sorted(players_list, key=lambda player: player["nick_first_last"])
    return sorted_list
