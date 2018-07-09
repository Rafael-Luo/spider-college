# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from SpiderForCollege.Citems import Citme

__author__ = 'lilu'

import scrapy
# 引入本地的模板



class MyScr(scrapy.Spider):

    # 设置全局唯一的name
    name = 'college'

    # 填写爬取地址
    start_urls = ['http://news.sina.com.cn/china/']

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = Citme()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="news-item  img-news-item"]'):
            # 获取div中的课程标题
            item['title'] = box.xpath('.//a/text()').extract()[0].strip()

            # 返回信息
            yield item