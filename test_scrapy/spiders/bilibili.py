# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/v1/dm/list.so?oid=48711416']

    def parse(self, response):
        a=response.xpath('//d/text()')


        for x in a:
            print(x.extract())
            with open('bilibili_danmu.csv','a',encoding='utf-8')as fp:
                fp.write(x.extract()+'\n')
