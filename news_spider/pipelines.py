# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging

import pymysql
from scrapy.exceptions import DropItem


def validate_item(item):
    if 'title' not in item:
        print("Missing name in %s" % item['url'])
        logging.error("Missing name in %s" % item['url'])
        return False
    elif item['title'].strip() == "":
        print("Empty name in %s" % item['url'])
        logging.error("Empty name in %s" % item['url'])
        return False

    if 'url' not in item:
        print("Missing url in %s" % item['title'])
        logging.error("Missing current_price in %s" % item['title'])
        return False

    return True


class ValidateItemsPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',
                                    passwd='123456', db='akali', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if validate_item(item):
            return item
        else:
            DropItem()
        title = item.get("title", "")
        url = item.get("url", "")
        hot_val = item.get("hot_val", "")
        sql = "insert into news(title, url, hot_val) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (title, url, hot_val))
        self.conn.commit()
