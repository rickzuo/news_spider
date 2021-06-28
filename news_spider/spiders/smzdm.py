import scrapy

from news_spider.items import SmzdmItem
from news_spider.utils.common import get_category_by_name


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://faxian.smzdm.com/json_more?filter=h4s0t0f0c0&page=1',
                  'https://faxian.smzdm.com/json_more?filter=h4s0t0f0c0&page=2',
                  'https://faxian.smzdm.com/json_more?filter=h4s0t0f0c0&page=3'
                  ]
    category_id = get_category_by_name(name)

    def parse(self, response):
        json_data =  response.json()

        for data in json_data:
            item = SmzdmItem()
            title = data["article_title"]
            url = data["article_url"]
            article_rating = data["article_rating"]
            # article_price = data["article_price"]
            article_comment = data["article_comment"]
            # article_content_all = data["article_content_all"]
            item["title"] = title
            item["url"] = url
            item["hot_val"] = f"评论数:{article_comment}"
            item["category_id"] = self.category_id
            item["rank"] = article_rating
            yield item
