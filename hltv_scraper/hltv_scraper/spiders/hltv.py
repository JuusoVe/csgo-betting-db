from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from parsers import parse_player_from_image_title_to_player_dict


class HLTVSpider(CrawlSpider):
    name = "hltv_scraper"

    start_urls = ["https://www.hltv.org/team/4608/stuff"]

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        image_elements = response.css('.bodyshot-team-img::attr(title)').getall()
        return {
            "result": image_elements,
        }


