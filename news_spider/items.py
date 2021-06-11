# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class NewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BaiduTopItem(Item):
    title = Field()
    url = Field()
    hot_val = Field()


class WeiboItem(Item):
    title = Field()
    url = Field()
    hot_val = Field()