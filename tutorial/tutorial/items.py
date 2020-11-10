import scrapy


class TutorialItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
