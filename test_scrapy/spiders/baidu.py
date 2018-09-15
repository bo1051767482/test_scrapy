# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        with open('baidu.html','w',encoding='utf-8')as fp:
            fp.write(response.body.decode('utf-8'))
