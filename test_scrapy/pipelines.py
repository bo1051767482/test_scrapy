# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# 倒入设置好的数据库信息
from test_scrapy.settings import mongo_host,mongo_name,mongo_port,mongo_table


class TestScrapyPipeline(object):

    # 定义初始化属性
    def __init__(self):
        host=mongo_host
        port=mongo_port
        data_name=mongo_name
        table_name=mongo_table
        # 连接数据库
        client=pymongo.MongoClient(host=host,port=port)
        # 连接指定库
        mydb=client[data_name]
        # 提交地址
        self.post=mydb[table_name]

    def process_item(self, item, spider):
        # 插入数据item来自spider里的yeild过来的
        data=dict(item)
        # 提交到数据库的表里插入数据
        self.post.insert(data)
        # print('插入数据')
        return item

class Web_RankingPipeline(object):
    def process_item(self, item, spider):
        # 将数据转换为字典
        data = dict(item)
        # 连接数据库
        client=pymongo.MongoClient(host='localhost',port=27017)
        # 链接库
        db=client['web']
        # 链接表
        set=db['web_ranking']
        # 写入数据
        set.insert(data)
        # 到数据库里查询数据
        # info = set.find_one({'web_ranking': '4'})
        # print(type(info), info)
        return item

    # def __init__(self):
    #     host=mongo_host
    #     port=mongo_port
    #     data_name=mongo_name
    #     table_name=mongo_table
    #     # 连接数据库
    #     client=pymongo.MongoClient(host=host,port=port)
    #     # 连接指定库
    #     mydb=client['web']
    #     # 提交地址
    #     self.post=mydb['web_ranking']
    # def process_item(self, item, spider):
    #     # 插入数据item来自spider里的yeild过来的
    #     data = dict(item)
    #     # 提交到数据库的表里插入数据
    #     self.post.insert(data)
    #     # print('插入数据')
    #     return item