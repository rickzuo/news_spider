import json
import logging
import re
from datetime import datetime

import scrapy

from news_spider.items import GelonghuiItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class GelonghuiSpider(scrapy.Spider):
    name = 'gelonghui'
    allowed_domains = ['https://www.gelonghui.com']
    start_urls = ['https://www.gelonghui.com']
    category_id = get_category_by_name(name)

    def parse(self, response):
        hot_article_list = response.xpath("//section[@id='hot-article']/ul/li")
        for data in hot_article_list:
            item = GelonghuiItem()

            title = data.xpath('./p/a/text()').extract()
            href = data.xpath('./p/a/@href').extract()
            title = parse_list_item(title).replace("/n", "")
            url = f"{self.allowed_domains[0]}{parse_list_item(href)}"
            item["title"] = title
            item["url"] = url
            item["hot_val"] = ""
            item["rank"] = int(datetime.now().timestamp())
            item["category_id"] = self.category_id

            yield item
        # item_list = script_json["newsflashCatalogData"]["data"]["newsflashList"]["data"]["itemList"]
