# -*- coding: utf-8 -*-
import scrapy
from test_scrapy.items import TestScrapyItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        move_list=response.xpath("//ol[@class='grid_view']/li")
        for x in move_list:
            douban=TestScrapyItem()
            # 电影序号
            douban['serial_num']=x.xpath(".//div[@class='item']/div[@class='pic']/em/text()").extract_first()
            # # 电影名字
            douban['move_name']=x.xpath(".//div[@class='item']/div[@class='pic']/a/img/@alt").extract_first()
            # move_name = scrapy.Field()
            # # 电影介绍
            content=x.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                resault=''.join(i_content.split())
                # print(resault)
                douban['introduce'] = resault


            # 电影星级
            douban['start']=x.xpath(".//span[@class='rating_num']/text()").extract_first()

             # 电影评价
            douban['evaluate']=x.xpath(".//div[@class='star']/span[4]/text()").extract_first()

             # 电影描述
            douban['describe']=x.xpath(".//span[@class='inq']/text()").extract_first()
            # print(douban)
            # 把整理好的数据扔给piplines  管道里
            yield douban
        next_link=response.xpath("//span[@class='next']/a/@href")
        # print(next_link.extract_first())
        if next_link:
            # 取出翻页链接
            next_link=next_link.extract_first()
            # 从新请求  回钓函数parse继续进行爬   函数不用加括号
            yield  scrapy.Request('https://movie.douban.com/top250'+next_link,callback=self.parse)

