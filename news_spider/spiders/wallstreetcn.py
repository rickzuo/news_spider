import scrapy

from news_spider.items import WallstreetcnItem
from news_spider.utils.common import get_category_by_name


class WallstreetcnSpider(scrapy.Spider):
    name = 'wallstreetcn'
    allowed_domains = ['https://api.wallstcn.com']
    start_urls = ['https://api.wallstcn.com/apiv1/content/information-flow?channel=global&accept=article&limit=20&action=upglide']
    category_id = get_category_by_name(name)

    def parse(self, response):
        json_data = response.json()
        res_list = json_data["data"]["items"]
        for index,res in enumerate(res_list):
            item = WallstreetcnItem()
            resource = res["resource"]
            title = resource["title"]
            display_time = resource["display_time"]
            url = resource["uri"]
            hot_val = resource["author"]["display_name"]
            item["title"] = title
            item["url"] = url
            item["hot_val"] = hot_val
            item["rank"] = index + 1
            item["category_id"] = self.category_id
            yield item

