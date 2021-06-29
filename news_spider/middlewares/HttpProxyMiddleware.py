# -*- coding: utf-8 -*-
import random
import time

from scrapy import signals


class StaticProxyMiddleware(object):

    def __init__(self):
        self.proxy_list = ['http://127.0.0.1:1087']

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def process_request(self, request, spider):
        if not hasattr(spider, "proxy"):
            return
        print("spider.proxy:", spider.proxy)
        # 该爬虫是否需要代理
        if not spider.proxy:
            return
        self.set_request_ip(request)

    # 设置request的代理ip
    def set_request_ip(self, request):
        proxy = random.choice(self.proxy_list)
        print('使用代理,地址为%s' % proxy)
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        return response

    # 代理出问题
    def process_exception(self, request, exception, spider):
        return
