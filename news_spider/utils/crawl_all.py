# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 11:38 上午
# @Author  : rickzuo
# @File    : crawl_all.py
# @Software: PyCharm
from scrapy.commands import ScrapyCommand

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list:
            self.crawler_process.crawl(name, **opts.__dict__)
        self.crawler_process.start()
