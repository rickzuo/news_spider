import scrapy

from news_spider.items import PengPaiItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class PengpaiSpider(scrapy.Spider):
    name = 'pengpai'
    allowed_domains = ['thepaper.cn']
    start_urls = ['https://www.thepaper.cn/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        li_list = response.xpath("//ul[@id='listhot0']/li")
        for index, li in enumerate(li_list):
            href = li.xpath("./a/@href").extract()
            title = li.xpath("./a/text()").extract()
            item = PengPaiItem()
            item["title"] = parse_list_item(title)
            item["url"] = f"{self.start_urls[0]}{parse_list_item(href)}"
            item["category_id"] = self.category_id
            item["rank"] = index + 1
            yield item
