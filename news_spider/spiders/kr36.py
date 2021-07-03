import json
import logging

import scrapy

from news_spider.items import Kr36Item
from news_spider.utils.common import get_category_by_name, parse_list_item


class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['www.36kr.com/newsflashes']
    start_urls = ['https://36kr.com/newsflashes']
    category_id = get_category_by_name(name)

    def parse(self, response):
        script_list = response.xpath("//script[contains(text(),'window.initialState=')]")
        if not script_list:
            logging.error("crawl 36kr fail:", script_list)
            return

        script_data = script_list[0].extract()
        import re
        re_data = re.findall("initialState=(.*?)</script>",script_data,re.S)
        script_data = re_data[0]
        script_json = json.loads(script_data)
        item_list = script_json["newsflashCatalogData"]["data"]["newsflashList"]["data"]["itemList"]
        for data in item_list:
            item = Kr36Item()
            template_material = data["templateMaterial"]
            title = template_material["widgetTitle"]
            ptime = template_material["publishTime"]
            item_id = template_material["itemId"]
            widget_content = template_material["widgetContent"]

            item["title"] = title
            url = f"{self.allowed_domains[0]}/{item_id}"
            item["url"] = url
            item["rank"] = ptime
            item["category_id"] = self.category_id
            yield item



    def parse2(self, response):
        news_list = response.xpath("//div[@class='newsflash-item']")
        for new in news_list:
            item = Kr36Item()
            href = new.xpath("./a[@class='item-title']/@href").extract()
            title = new.xpath("./a[@class='item-title']/text()").extract()
            url_path = parse_list_item(href)
            title = parse_list_item(title)
            item["title"] = title
            url = f"{self.allowed_domains[0]}{url_path}"
            item["url"] = url
            item["rank"] = 0
            item["category_id"] = self.category_id
            # href = new.xpath("./div[@class='item-desc']/a[@class='link']/@href").extract()
            print(url, title)
            yield item
