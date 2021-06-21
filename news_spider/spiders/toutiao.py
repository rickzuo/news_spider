import logging

import requests
import scrapy

from news_spider.items import ToutiaoItem
from news_spider.utils.common import get_category_by_name


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    start_urls = [
        'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398996&max_behot_time=0&category=pc_profile_channel']
    category_id = get_category_by_name(name)

    def parse(self, response):
        news_list = response.json()
        if news_list["message"] != "success":
            logging.error("crawl toutiao fail:", news_list)
            return
        nlist = news_list["data"]
        for index, new in enumerate(nlist):
            item = ToutiaoItem()
            title = new["title"]
            url = new["url"]
            hot_val = new["source"]
            abstract = new["Abstract"]

            item["title"] = title
            item["url"] = url
            item["hot_val"] = hot_val
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            yield item
