import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FlipbooksSpider(CrawlSpider):
    name = 'flipbooks'
    allowed_domains = ['flip.kz']
    start_urls = ['https://www.flip.kz/']

    rules = (Rule(LinkExtractor(allow=r'flip.kz'),
                  callback='parse_item', follow=True),)

    def parse_item(self, response):
        url = response.request.url
        if 'flip.kz/catalog?prod' in url:
            print('Found item link: ', url)
