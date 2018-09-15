# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from bs4 import BeautifulSoup


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['www.stat-nba.com/query.php']
    start_urls = []
    # 分页请求
    page = 0
    for num in range(0,2):
        url='http://www.stat-nba.com/query.php?page={}&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=20#label_show_result'.format(page)
        page += 1
        start_urls.append(url)


    def parse(self, response):
        # 读内容
        content=response.body.decode('utf-8')
        # 转为xml
        tree=etree.HTML(content)
        # 标签选择器
        list=tree.xpath('//tbody/tr')

        # 清洗存储文件
        for x in list:
            name=x.xpath('./td/a/text()')
            tdlis=x.xpath('./td/text()')
            info=name[0]+'  '+'篮板'+tdlis[14]+'   '+'助攻'+tdlis[17]+'   '+'得分'+tdlis[22]+'\n'
            with open('清洗过后的nba.csv','a',encoding='utf-8')as fp:
                fp.write(info)



