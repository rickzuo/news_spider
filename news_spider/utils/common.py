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
    elif name == "pengpai":
        return 8
    elif name == "tengxun":
        return 9
    elif name == "wangyi":
        return 16
    elif name == "toutiao":
        return 17
    elif name == "36kr":
        return 18
    elif name == "sspai":
        return 21
    elif name == "huxiu":
        return 20
    elif name == "ithome":
        return 19
    elif name == "cnbeta":
        return 22
    elif name == "xueqiu":
        return 23
    elif name == "wallstreetcn":
        return 24
    elif name == "yicai":
        return 25
    elif name == "gelonghui":
        return 26
    elif name == "smzdm":
        return 27
    elif name == "juejin":
        return 28
    elif name == "v2ex":
        return 29


