# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com/cinemas']
    # start_urls = ['http://maoyan.com/cinemas/']
    start_urls = []
    for num in range(0, 20):
        page=0
        url = 'http://maoyan.com/cinemas?offset={}'.format(page)
        page += 12
        start_urls.append(url)

    def parse(self, response):
        content=response.body.decode('utf-8')
        # 实例化BeautifulSoup
        soup = BeautifulSoup(content, 'lxml')
        # css选择器
        div_list=soup.select('div.cinema-info')
        for  x in div_list:
            name=x.select('a')[0].get_text()
            add=x.select('p')[0].get_text()
            info='名字:  '+name+'\n'+add+'\n'+'\n'+'\n'
            with open('blog.txt','a+',encoding='utf-8')as fp:
                fp.write(info)

