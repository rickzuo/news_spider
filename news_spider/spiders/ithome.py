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
        for index,new in enumerate(news_list):
            item = IthomeItem()

            href = new.xpath("./a/@href").extract()
            title = new.xpath("./a/text()").extract()
            create_time = new.xpath("./b/text()").extract()

            url = parse_list_item(href)
            title = parse_list_item(title)
            hot_val = parse_list_item(create_time).replace(" ",":")

            item["title"] = title
            item["hot_val"] = hot_val
            item["url"] = url
            item["rank"] = index + 1
            item["category_id"]  = self.category_id

            yield item
