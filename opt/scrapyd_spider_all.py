# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 1:34 下午
# @Author  : rickzuo
# @File    : scrapyd_spider_all.py
# @Software: PyCharm
import time

import requests

base_url = "http://localhost:6800"
project = "default"


def get_all_spiders():
    url = f"{base_url}/listspiders.json?project={project}"
    print("url:", url)
    resp = requests.get(url)
    print(resp.json())
    return resp.json()


def get_scrapy_status():
    url = f"{base_url}/daemonstatus.json"
    print("url:", url)
    resp = requests.get(url)
    return resp.json()


def run_spider(spider_name=None):
    spider_names = []
    if not spider_name:
        spiders_info = get_all_spiders()
        spider_names = spiders_info.get("spiders")
        print("spiders:", spiders_info)
    else:
        spider_names.append(spider_name)

    for spider_name in spider_names:
        url = f"{base_url}/schedule.json"
        post_data = {
            "project": project,
            "spider": spider_name,
        }
        print("url:", url)
        resp = requests.post(url, data=post_data)
        print(resp.json())

def print_status():
    status = get_scrapy_status()
    pending = status["pending"]
    running = status["running"]
    finished = status["finished"]
    while pending != 0 or running != 0:
        status = get_scrapy_status()
        print(status)
        pending = status["pending"]
        running = status["running"]
        time.sleep(1)

def setup():
    run_spider()
    print_status()

if __name__ == '__main__':
    setup()

