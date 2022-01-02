import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from src.utils.parsers import parse_real_name, parse_nickname, parse_player_from_image_title, parse_hltv_id_from_url

base_url = "https://www.hltv.org/"

def scrape_player(hltv_id):
    url = base_url + 'player/' + hltv_id + "/stuff"
    # hltv returns 404 if you dont put anything after the id, but it can be anything.
    print('scraping player from url: ' + url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    real_name_elements = soup.find_all("div", class_="player-realname")
    if not real_name_elements:
      real_name_elements = soup.find_all("div", class_="playerRealname")
    if not real_name_elements:
      return 'no real name found for player ' + hltv_id
    real_name_string = real_name_elements[0].text
    parsed_real_name = parse_real_name(real_name_string)

    nickname_elements = soup.find_all("div", class_="player-nickname")
    if not nickname_elements:
      nickname_elements = soup.find_all("h1", class_="playerNickname")
    if not nickname_elements:
      return 'no nick name found for player ' + hltv_id
    parsed_nick_name = parse_nickname(nickname_elements[0].text)
    player = {
     "first_name": parsed_real_name[0],
     "last_name": parsed_real_name[1],
     "nickname": parsed_nick_name,
     "hltv_id": hltv_id
    }
    return player

def scrape_team_players(hltv_id):
    url = base_url + 'team/' + hltv_id + "/stuff"
    # hltv returns 404 if you dont put anything after the id, but it can be anything.
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    page = response.html.html
    soup = BeautifulSoup(page, "html.parser")
    players = soup.find("div", class_="bodyshot-team g-grid")
    team = []
    for player in players.children:
      player_profile_url = player.get('href')
      hltv_id = parse_hltv_id_from_url(player_profile_url)
      image = player.find("img", class_="bodyshot-team-img")
      title = image.get('title')
      player = parse_player_from_image_title(title)
      player['hltv_id'] = hltv_id
      team.append(player)
    return team
