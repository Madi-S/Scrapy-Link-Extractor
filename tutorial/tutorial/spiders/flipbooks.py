import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TutorialItem


class FlipbooksSpider(CrawlSpider):
    name = 'flipbooks'
    allowed_domains = ['flip.kz']
    start_urls = ['https://www.flip.kz/']
    rules = (Rule(LinkExtractor(allow=''),
                  callback='parse_item', follow=True),)

    def parse_item(self, response):
        if 'catalog' in str(response.url):

            item = TutorialItem()
            item['title'] = response.xpath('//h1/text()').get()
            item['price'] = response.xpath(
                '//span[@class="text_att"]//b/text()').get()
            item['description'] = response.xpath(
                '//span[@itemprop="description"]/text()').get()

            yield item
