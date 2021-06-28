import json

import scrapy

from news_spider.items import JuejinItem
from news_spider.utils.common import get_category_by_name


class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.cn']
    start_urls = ['https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed/']
    category_id = get_category_by_name(name)

    def start_requests(self):
        cls = self.__class__
        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")

        post_data = {"id_type": 2, "client_type": 2608, "sort_type": 3, "cursor": "0", "limit": 20}
        for url in self.start_urls:
            yield scrapy.Request(url, method='POST',
                                 callback=self.parse,
                                 body=json.dumps(post_data),
                                 headers={'Content-Type': 'application/json'})

    def parse(self, response):
        json_ret = response.json()
        json_data = json_ret["data"]
        for item_data in json_data:
            item_type = item_data["item_type"]
            if item_type != 2:
                continue
            item = JuejinItem()
            item_info = item_data["item_info"]
            category = item_info["category"]
            article_id = item_info["article_id"]
            category_name = category["category_name"]
            article_info = item_info["article_info"]

            # author_name = item_info["author_name"]
            hot_val = article_info["view_count"]
            title = article_info['title']
            title = f"({category_name}){title}"
            url = f"https://juejin.cn/post/{article_id}"
            rtime = article_info["rtime"]
            item["title"] = title
            item["url"] = url
            item["hot_val"] = hot_val
            item["rank"] = rtime
            item["category_id"] = self.category_id

            yield item