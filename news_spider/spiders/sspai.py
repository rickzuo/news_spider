import scrapy

from news_spider.items import SspaiItem
from news_spider.utils.common import get_category_by_name


class SspaiSpider(scrapy.Spider):
    name = 'sspai'
    allowed_domains = ['sspai.com']
    start_urls = [
        'https://sspai.com/api/v1/article/tag/page/get?limit=20&offset=0&tag=%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0&released=false']
    category_id = get_category_by_name(name)

    def parse(self, response):
        json_data = response.json()
        news_list = json_data["data"]
        for index, new in enumerate(news_list):
            item = SspaiItem()
            title = new["title"]
            id = new["id"]
            url = f"https://sspai.com/post/{id}"
            author = new["author"]
            if author:
                hot_val = author["nickname"]
                item["hot_val"] = hot_val

            item["title"] = title
            item["url"] = url
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            yield item
