from datetime import datetime

import scrapy

from news_spider.items import YicaiItem
from news_spider.utils.common import get_category_by_name


class YicaiSpider(scrapy.Spider):
    name = 'yicai'
    allowed_domains = ['https://www.yicai.com']
    start_urls = ['https://www.yicai.com/api/ajax/getjuhelist?action=news&page=1&pagesize=25']
    category_id = get_category_by_name(name)
    def parse(self, response):
        json_data = response.json()
        for data in json_data:
            item = YicaiItem()
            title = data["NewsTitle"]
            author = data["NewsAuthor"]
            mtime = data["LastDate"]
            modify_date = datetime.strptime(mtime, '%Y-%m-%dT%H:%M:%S')
            url = f"{self.allowed_domains[0]}{data['url']}"
            item["title"] = title
            item["url"] = url
            item["rank"] = int(modify_date.timestamp())
            item["hot_val"] = author
            item["category_id"] = self.category_id
            yield item
