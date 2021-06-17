# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:47 上午
# @Author  : rickzuo
# @File    : main.py
# @Software: PyCharm
import scrapy
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'baidu'])
# execute(['scrapy', 'crawl_all'])
