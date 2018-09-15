# -*- coding: utf-8 -*-
import scrapy
# from lxml import  etree
# from scrapy_redis.spiders import RedisSpider
from test_scrapy.items import web_rankingItem

class Web_rankingSpider(scrapy.Spider):
    name = 'web_ranking'
    allowed_domains = ['top.chinaz.com']
    start_urls = ['http://top.chinaz.com/hangye/']
    # redis_key = "web_rankingSpider:start_urls"
    # custom_settings = {
    #     'ITEM_PIPELINES': {'test_scrapy.pipelines.Web_RankingPipeline': 300, }
    # }
    def parse(self, response):
            weblist=response.xpath("//ul[@class='listCentent']/li")
            for item in weblist:
                # print(item)
                web=web_rankingItem()
                web['web_ranking']=item.xpath(".//div[@class='RtCRateCent']/strong/text()").extract_first()
                web['web_name']=item.xpath(".//a[@class='pr10 fz14']/text()").extract_first()
                web['web_integral']=item.xpath(".//div[@class='RtCRateCent']/span/text()").extract_first()
                web['web_describe']=item.xpath(".//div[@class='CentTxt']/p/text()").extract_first()
                yield web

                # 翻页  继续爬
            next_link = response.xpath("//div[@class='ListPageWrap']/a[11]/@href")
            # print(next_link)

            if next_link:
                # 取出翻页链接
                next_link = next_link.extract_first()
                print(next_link)
                # 从新请求  回钓函数parse继续进行爬   函数不用加括号
                yield scrapy.Request('http://top.chinaz.com/hangye/' + next_link, callback=self.parse)
            else:
                yield scrapy.Request('http://top.chinaz.com/hangye/' + 'index_19.html', callback=self.parse)

