import scrapy

from news_spider.items import WeiboItem
from news_spider.utils.common import parse_list_item, get_category_by_name


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['https://s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot/']
    category_id = get_category_by_name(name)

    def parse(self, response):
        tbody = response.xpath("//div[@id='pl_top_realtimehot']/table/tbody")
        tr_list = tbody.xpath("./tr")
        for tr in tr_list:
            item = WeiboItem()
            td_list = tr.xpath("./td")
            if len(td_list) <= 1:
                continue
            td_info = td_list[1]
            td_href = parse_list_item(td_info.xpath("./a/@href").extract())
            td_title = parse_list_item(td_info.xpath("./a/text()").extract())
            hot_val = parse_list_item(td_info.xpath("./span/text()").extract())
            url = f"{self.allowed_domains[0]}{td_href}"
            if "javascript:void(0)" in url:
                continue

            item["url"] = url
            item["title"] = td_title
            item["hot_val"] = hot_val
            item["category_id"] = self.category_id
            item["rank"] = hot_val
            yield item
