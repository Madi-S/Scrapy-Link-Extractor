import scrapy


class FlipbooksSpider(scrapy.Spider):
    name = 'flipbooks'
    allowed_domains = ['flip.kz']
    start_urls = ['http://flip.kz/']

    def parse(self, response):
        pass
