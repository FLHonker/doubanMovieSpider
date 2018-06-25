# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入 sys 模块
import sys
# 设置字符集变量 default_encoding 为 utf-8
default_encoding = 'utf-8'
# 判断系统当前默认字符是否为指定的 utf-8
if sys.getdefaultencoding() != default_encoding:
    # 使用 reload()函数重新加载 sys 模块
    reload(sys)
# 设置系统默认字符集为 utf-8
sys.setdefaultencoding(default_encoding)

class DoubanmoviePipeline(object):
    # process_item()函数,处理每一个采集到的电影数据
    def process_item(self, item, spider):
        print '排名 TOP:' + item['rank'][0]
        print '电影名称:' + item['title'][0]
        print '详情链接:' + item['link'][0]
        print '豆瓣评分:' + item['rating'][0] + ' ('+ item['participants'][0] +') '
        print '最新评论:' + item['quote'][0]
        # 返回 item,开始接收下一条电影数据进行处理
        return item