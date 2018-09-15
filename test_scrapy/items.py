# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


# <editor-fold desc="Description">
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
class ExampleItem(Item):
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()

class ExampleLoader(ItemLoader):
    default_item_class = ExampleItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
# </editor-fold>

import scrapy


class TestScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 电影序号
    serial_num=scrapy.Field()
    # 电影名字
    move_name=scrapy.Field()
    # 电影介绍
    introduce=scrapy.Field()
    # 电影星级
    start=scrapy.Field()
    # 电影评价
    evaluate=scrapy.Field()
    # 电影描述
    describe=scrapy.Field()
class web_rankingItem(scrapy.Item):
    web_ranking=scrapy.Field()
    web_name=scrapy.Field()
    web_integral =scrapy.Field()
    web_describe=scrapy.Field()