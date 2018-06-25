# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 导入 scrapy 框架 item 模块中的 Item 和 Field 对象
import scrapy
from scrapy.item import Item, Field

# MovieItem 类,继承 scrapy.Item 父类
# 实现定义抓取的每一条信息的对象
class MovieItem(scrapy.Item):
    # 定义需要获取的电影信息属性
    rank = scrapy.Field() # 排名序号
    title = scrapy.Field() # 电影名称
    link = scrapy.Field() # 电影详情链接地址
    rating = scrapy.Field() # 电影评分
    participants = scrapy.Field() # 参评人数
    quote = scrapy.Field() # 最新评论
