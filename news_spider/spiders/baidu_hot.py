from urllib.parse import unquote

import scrapy
from lxml import etree

from news_spider.items import BaiduTopItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class BaiduHotSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['http://top.baidu.com/buzz?b=1']
    start_urls = ['http://top.baidu.com/buzz?b=1/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        text = response.text
        tree = etree.HTML(text)
        table = tree.xpath('//table[@class="list-table"]')[0]
        tr_list = table.xpath('//tr')
        for index,tr in enumerate(tr_list):
            item = BaiduTopItem()
            td_list = tr.xpath('./td[@class="keyword"]')
            if not td_list:
                continue
            td = td_list[0]
            title = td.xpath('./a[@class="list-title"]/text()')
            tc = tr.xpath('./td[@class="tc"]')[0]
            tc_href = tc.xpath('./a/@href')
            # tc_title = tc.xpath('./a/text()')
            # detail_url = td.xpath('//a[@class="list-title"]/@href')

            td_last = tr.xpath('./td[@class="last"]/span/text()')
            item["title"] = parse_list_item(title)
            href = parse_list_item(tc_href)
            item["url"] = unquote(href,"GBK")
            item["hot_val"] = parse_list_item(td_last)
            item["category_id"] = self.category_id
            item["rank"] = index + 1
            yield item
