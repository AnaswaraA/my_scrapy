# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AbrasivesparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    product_name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    SKU = scrapy.Field()
    breadcrumbs = scrapy.Field()
    MfgPartNo=scrapy.Field()


