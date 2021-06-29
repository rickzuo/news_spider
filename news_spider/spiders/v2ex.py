import requests
import scrapy

from news_spider.items import V2exItem
from news_spider.utils.common import get_category_by_name


class V2exSpider(scrapy.Spider):
    name = 'v2ex'
    allowed_domains = ['www.v2ex.com']
    start_urls = ['https://www.v2ex.com/api/topics/hot.json', 'https://www.v2ex.com/api/topics/latest.json']
    category_id = get_category_by_name(name)
    proxy = True

    def parse(self, response):
        json_data = response.json()
        for data in json_data:
            item = V2exItem()
            title = data["title"]
            url = data["url"]
            replies = data["replies"]
            last_modified = data["last_modified"]
            item["title"] = title
            item["url"] = url
            item["hot_val"] = replies
            item["rank"] = last_modified
            item["category_id"] = self.category_id
            yield item
