import datetime

import scrapy

from news_spider.items import IthomeItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com']
    start_urls = ['http://ithome.com/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        news_list = response.xpath("//div[@id='nnews']//li[@class='n']")
        for data in news_list:
            item = IthomeItem()

            href = data.xpath("./a/@href").extract()
            title = data.xpath("./a/text()").extract()
            create_time = data.xpath("./b/text()").extract()

            url = parse_list_item(href)
            title = parse_list_item(title)
            hot_val = parse_list_item(create_time).replace(" ",":")

            item["title"] = title
            item["hot_val"] = hot_val
            today = datetime.date.today()
            create_date = datetime.datetime.strptime(f"{today} {hot_val}", '%Y-%m-%d %H:%M')
            ctime = int(create_date.timestamp())
            item["url"] = url
            item["rank"] = ctime
            item["category_id"]  = self.category_id

            yield item
