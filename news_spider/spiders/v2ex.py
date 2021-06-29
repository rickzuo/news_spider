import requests
import scrapy

from news_spider.items import V2exItem
from news_spider.utils.common import get_category_by_name


class V2exSpider(scrapy.Spider):
    name = 'v2ex'
    allowed_domains = ['www.v2ex.com']
    start_urls = ['https://www.v2ex.com/api/topics/hot.json']
    category_id = get_category_by_name(name)

    def start_requests(self):
        cls = self.__class__
        if not self.start_urls and hasattr(self, 'start_url'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")
        headers = {
            ":authority": "www.v2ex.com",
            "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            ":method": "GET",
            ":path": "/api/topics/hot.json",
            ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"
        }
        for url in self.start_urls:
            print("url:", url)
            response = requests.get(url)
            print(response.json())

            yield scrapy.Request(url, headers=headers, dont_filter=False)

    def parse(self, response):
        json_data = response.json()
        print("111", json_data)
        for data in json_data:
            item = V2exItem()
            title = data["title"]
            url = data["url"]
            replies = data["replies"]
            item["title"] = title
            item["url"] = url
            item["hot_val"] = replies
            item["category_id"] = self.category_id
            print(item)
