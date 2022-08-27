from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hltv_scraper.parsers import parse_player_image_title_to_player_dict


class HLTVSpider(CrawlSpider):
    name = "hltv_scraper"

    start_urls = ["https://www.hltv.org/team/4608/stuff"]

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        image_title_strings = response.css('.bodyshot-team-img::attr(title)').getall()
        players = []
        for title_string in image_title_strings:
          players.append(parse_player_image_title_to_player_dict(title_string))


        return {
            "result": players,
        }


