# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = []

    for num in range(1,338):
        page=str((num-1)*10)
        url='https://hr.tencent.com/position.php?&start={}#a'.format(page)
        start_urls.append(url)

    def parse(self, response):
        content=response.body.decode('utf-8')
        soup=BeautifulSoup(content,'lxml')
        tr_list = soup.select('table.tablelist > tr')
        for tr in tr_list:
            if tr.get('class')[0] == 'even' or tr.get('class')[0] == 'odd':
                name = tr.select('td')[0].get_text()
                href = tr.select('td a')[0].get('href')
                type = tr.select('td')[1].get_text()
                num = tr.select('td')[2].get_text()
                location = tr.select('td')[3].get_text()
                time = tr.select('td')[4].get_text()
                info='职位：'+name+'--'+'类型:'+type+'--'+'人数:'+num+'--'+'地点：'+location+'--'+'时间：'+time+'\n'
                with open('tencent_recruitment.csv','a+',encoding='utf-8')as f:
                    f.write(info)

