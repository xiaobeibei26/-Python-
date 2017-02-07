# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#小区名字
    rental = scrapy.Field()#租金
    distance = scrapy.Field()# 距离地铁的远近
    area = scrapy.Field()#面积
    room_number=scrapy.Field()#几室几厅
    floor =scrapy.Field()#在几层
    direction = scrapy.Field()#房屋朝向
    year_build=scrapy.Field()#房子的建造时间

    pass
