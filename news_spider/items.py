# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class NewsSpiderBaseItem(scrapy.Item):
    title = Field()
    url = Field()
    hot_val = Field()


class BaiduTopItem(NewsSpiderBaseItem):
    pass


class WeiboItem(NewsSpiderBaseItem):
    pass


class ZhihuItem(NewsSpiderBaseItem):
    pass
