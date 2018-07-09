# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'lilu'

import scrapy

# 编写model模板
class Citme(scrapy.Item):
    # 储存标题
    title = scrapy.Field()