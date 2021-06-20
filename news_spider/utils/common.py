# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 5:25 下午
# @Author  : rickzuo
# @File    : common.py
# @Software: PyCharm

def parse_list_item(data):
    if len(data) == 0:
        return ""
    return data[0].strip()

def get_category_by_name(name):
    if name == "baidu":
        return 2
    elif name == "zhihu":
        return 7
    elif name == "weibo":
        return 5
