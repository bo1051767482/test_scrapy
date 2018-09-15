# -*- coding: utf-8 -*-
import scrapy
# /日志
# import logging
#
# logging.basicConfig(filename='./日志.log',
#                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG, filemode='a',
#                     datefmt='%Y-%m-%d%I:%M:%S %p')


class DianpingSpider(scrapy.Spider):
    name = 'dianping'
    allowed_domains = ['baidu.com']
    start_urls = ['http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/shoptextcss/review.HP7M7KOIBe.svg']
    def parse(self, response):
        a=response.xpath(r'//text()').extract()
        print(a)


