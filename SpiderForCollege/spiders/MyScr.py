# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging



from SpiderForCollege.Citems import Citme
from SpiderForCollege.logs.Logging import load_my_logging_cfg

__author__ = 'liqian'

import scrapy


# 引入本地的模板


class MyScr(scrapy.Spider):

    load_my_logging_cfg()
    # 设置全局唯一的name
    name = 'college'

    # 填写爬取地址
    urls = ['http://gaokao.chsi.com.cn/sch/search.do?searchType=1&start=0']


    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = Citme()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="news-item  img-news-item"]'):
            # 获取div中的课程标题
            item['name'] = box.xpath('//tr/td[1]').extract()[0].strip()



            filename = 'mingyan-%s.html'   # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html

            with open(filename, 'wb') as f:  # python文件操作，不多说了；

                f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！


            self.log('保存文件: %s' % filename)  # 打个日志
            # 返回信息
            yield item

