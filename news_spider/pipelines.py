# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from datetime import datetime

import pymysql
from scrapy.exceptions import DropItem

from news_spider import settings


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
    def process_item(self, item, spider):
        if validate_item(item):
            return item
        else:
            DropItem()


class MysqlDbPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host=settings.MYSQL_DB_HOST,
                                    user=settings.MYSQL_DB_USER,
                                    passwd=settings.MYSQL_DB_PASSWORD,
                                    db=settings.MYSQL_DB_NAME
                                    , charset='utf8')
        self.cur = self.conn.cursor()

    def get_by_title(self, title):
        sql = "select id from news_news where title = %s "
        self.cur.execute(sql, (title,))
        exist = self.cur.fetchone()
        return exist

    def update_or_create(self, title, url, hot_val, category_id):
        instance = self.get_by_title(title)
        if instance:
            self.update(title, url,hot_val)
        else:
            self.create(title, url, hot_val, category_id)

    def update(self, title, url, hot_val):
        sql = "update  news_news set url = %s,hot_val = %s,updated_date = %s where title = %s "
        updated_date = datetime.now()
        self.cur.execute(sql, (url, hot_val, updated_date, title))
        self.conn.commit()

    def create(self, title, url, hot_val, category_id):
        sql = "insert into news_news(title, url, hot_val,created_date,updated_date,category_id) " \
              "VALUES (%s, %s, %s,%s,%s,%s)"
        created_date = datetime.now()
        updated_date = datetime.now()
        self.cur.execute(sql, (title, url, hot_val, created_date, updated_date, category_id))
        self.conn.commit()

    def process_item(self, item, spider):
        title = item.get("title", "")
        url = item.get("url", "")
        hot_val = item.get("hot_val", "")
        category_id = item.get("category_id", 1)
        self.update_or_create(title, url, hot_val, category_id)
