import scrapy

from news_spider.items import WangYiItem
from news_spider.utils.common import get_category_by_name


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['news.163.com']
    base_url = "https://c.m.163.com/news/a/{}.html"
    start_urls = ['https://gw.m.163.com/nc-main/api/v1/hqc/no-repeat-hot-list']
    category_id = get_category_by_name(name)

    def parse(self, response):
        news_list = response.json()
        code = news_list["code"]
        if code != 0:
            return
        items = news_list["data"]["items"]
        for index, new in enumerate(items):
            item = WangYiItem()
            source = new["source"]
            title = new["title"]
            hot_value = new["hotValue"]
            source = new["source"]
            contentId = new["contentId"]
            url = self.base_url.format(contentId)
            item["title"] = title
            item["url"] = url
            item["hot_val"] = hot_value
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            yield item
