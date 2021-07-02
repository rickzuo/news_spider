import json
import logging

import scrapy

from news_spider.items import HuxiuItem
from news_spider.utils.common import get_category_by_name


class HuxiuSpider(scrapy.Spider):
    name = 'huxiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['https://www.huxiu.com/article/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        script_list = response.xpath("//script[contains(text(),'__INITIAL_STATE__')]")
        if not script_list:
            logging.error("crawl huxiu fail:",script_list)
            return
        script_data = script_list[0].extract()
        # script_data = script_data.replace("<script>window.__INITIAL_STATE__=","")
        import re
        re_data = re.findall("TIAL_STATE__=(.*?);",script_data,re.S)
        script_data = re_data[0]
        script_json = json.loads(script_data)
        articles = script_json["article"]
        data_list = articles["articles"]["dataList"]
        for data in data_list:
            item = HuxiuItem()
            title = data["title"]
            username = data["user_info"]["username"]
            share_url = data["share_url"]
            page_sort = data["pageSort"]
            item["title"] = title
            item["hot_val"] = username
            item["url"] = share_url
            item["rank"] = page_sort
            item["category_id"] = self.category_id
            yield item
