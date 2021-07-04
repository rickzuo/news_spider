from datetime import datetime

import scrapy
from lxml import etree

from news_spider.items import XueqiuItem
from news_spider.utils.common import get_category_by_name, parse_list_item


class XueqiuSpider(scrapy.Spider):
    name = 'xueqiu'
    allowed_domains = ['http://xueqiu.com/hots/topic/rss']
    start_urls = ['http://xueqiu.com/hots/topic/rss/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        xmldoc = etree.fromstring(str.encode(response.text))
        res_list = xmldoc.xpath("//item")
        for res in res_list:
            item = XueqiuItem()
            title = parse_list_item(res.xpath("./title/text()"))
            url = parse_list_item(res.xpath("./guid/text()"))
            nsmap = {"dc": 'http://purl.org/dc/elements/1.1/'}
            create_at = res.xpath("./dc:date/text()", namespaces=nsmap)[0]
            create_date = datetime.strptime(create_at, '%Y-%m-%dT%H:%M:%SZ')
            creator = parse_list_item(res.xpath("./dc:creator/text()", namespaces=nsmap))
            item["title"] = title
            item["url"] = url
            item["hot_val"] = creator
            item["rank"] = int(create_date.timestamp())
            item["category_id"] = self.category_id
            yield item
