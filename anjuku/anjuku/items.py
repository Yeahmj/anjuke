# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukuItem(scrapy.Item):
    # define the fields for your item here like:
    # 数据来源
    data_source = scrapy.Field()
    # 生成时间
    timestamp = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 小区名称
    village = scrapy.Field()
    # 房租
    charge = scrapy.Field()
    # 方式 整租 合租
    fashion = scrapy.Field()
    # 房型
    house_type = scrapy.Field()
    # 位置
    address = scrapy.Field()
    # 装修
    fixture = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    direction = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 配置
    configure = scrapy.Field()
    # 描述
    desc = scrapy.Field()
    pass
