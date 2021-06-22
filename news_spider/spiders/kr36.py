import scrapy

from news_spider.items import Kr36Item
from news_spider.utils.common import get_category_by_name, parse_list_item


class A36krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['www.36kr.com']
    start_urls = ['https://36kr.com/newsflashes']
    category_id = get_category_by_name(name)

    def parse(self, response):
        news_list = response.xpath("//div[@class='newsflash-item']")
        for index, new in enumerate(news_list):
            item = Kr36Item()
            href = new.xpath("./a[@class='item-title']/@href").extract()
            title = new.xpath("./a[@class='item-title']/text()").extract()
            url_path = parse_list_item(href)
            title = parse_list_item(title)
            item["title"] = title
            url = f"{self.allowed_domains[0]}{url_path}"
            item["url"] = url
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            # href = new.xpath("./div[@class='item-desc']/a[@class='link']/@href").extract()
            print(url, title)
            yield item
