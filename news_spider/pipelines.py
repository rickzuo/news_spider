# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
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
    def process_item(self, item, spider):
        if validate_item(item):
            return item
        else:
            DropItem()
