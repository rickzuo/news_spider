import scrapy

from news_spider.items import CnbetaItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class CnbetaSpider(scrapy.Spider):
    name = 'cnbeta'
    allowed_domains = ['www.cnbeta.com']
    start_urls = ['https://www.cnbeta.com/top10.htm']
    category_id = get_category_by_name(name)

    def parse(self, response):
        news_list = response.xpath("//div[@class='item']")
        print("news_list:", news_list)
        for index, new in enumerate(news_list):
            item = CnbetaItem()
            href = new.xpath("./dl/dt/a/@href").extract()
            title = new.xpath("./dl/dt/a/text()").extract()
            hot_val = new.xpath("./div[@class='meta-data']/ul/li/text()").extract()
            url = parse_list_item(href)
            if "//hot" in url:
                url = url.replace("//", "")
            title = parse_list_item(title)
            hot_val = parse_list_item(hot_val)

            item["title"] = title
            item["hot_val"] = hot_val
            item["url"] = url
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            yield item
