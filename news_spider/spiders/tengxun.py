import scrapy

from news_spider.items import TxItem
from news_spider.utils.common import get_category_by_name


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['xw.qq.com']
    start_urls = ['https://xw.qq.com/api/proxy?charset=utf-8&url=http:%2F%2Fopenapi.inews.qq.com%2FgetQQNewsIndexAndItems%3Fchlid%3Dnews_news_twentyf%26refer%3Dmobilewwwqqcom%26srcfrom%3Dnewsapp%26otype%3Djson%26mergetop%3D1%26ext_action%3DFimgurl33,Fimgurl32,Fimgurl30']
    category_id = get_category_by_name(name)

    def parse(self, response):
        json_list = response.json()
        ret = json_list["ret"]
        if ret != 0 :
            return
        idlist = json_list["idlist"][0]
        news_list = idlist["newslist"]
        for index,new in enumerate(news_list):
            item = TxItem()
            abstract = new["abstract"]
            source = new["source"]
            orig_url = new["origUrl"]
            timestamp = new["timestamp"]

            surl = new["surl"]
            title = new["title"]
            item["title"]= title
            item["url"]= surl
            item["hot_val"]= source
            item["rank"] = timestamp
            item["category_id"] = self.category_id
            yield item

