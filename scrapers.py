import requests
from bs4 import BeautifulSoup
from parsers import parse_real_name, parse_nickname

base_url = "https://www.hltv.org/"

def scrape_player(hltv_id):
    url = base_url + 'player/' + hltv_id + "/stuff"
    print('scraping player from url: ' + url)
    # hltv returns 404 if you dont put anything after the id, but it can be anything.
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    real_name_elements = soup.find_all("div", class_="player-realname")
    if not real_name_elements:
      real_name_elements = soup.find_all("div", class_="playerRealname")
    if not real_name_elements:
      print('no real name found for player ' + hltv_id)
      return 'no real name found for player ' + hltv_id
    real_name_string = real_name_elements[0].text
    parsed_real_name = parse_real_name(real_name_string)

    nickname_elements = soup.find_all("div", class_="player-nickname")
    if not nickname_elements:
      nickname_elements = soup.find_all("h1", class_="playerNickname")
    if not nickname_elements:
      print('no nick name found for player ' + hltv_id)
      return 'no nick name found for player ' + hltv_id
    parsed_nick_name = parse_nickname(nickname_elements[0].text)

    player = {
     "first_name": parsed_real_name[0],
     "last_name": parsed_real_name[1],
     "nickname": parsed_nick_name,
     "hltv_id": hltv_id
    }
    return player