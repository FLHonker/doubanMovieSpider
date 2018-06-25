# -*- coding: utf-8 -*-

import sys  # 导入 sys 模块
# 设置字符集变量 default_encoding 为 utf-8
default_encoding = 'utf-8'
# 判断系统当前默认字符是否为指定的 utf-8
if sys.getdefaultencoding() != default_encoding:
    reload(sys) # 使用 reload()函数重新加载 sys 模块
sys.setdefaultencoding(default_encoding)    # 设置系统默认字符集为 utf-8
# 导入 scrapy 框架 spider 模块中的 BaseSpider 对象
import scrapy
# 导入当前工程 items 模块(items.py)中的 MovieItem 类
from doubanMovie.items import MovieItem
from scrapy import Request

# MovieSpider 类,继承 BaseSpider 父类
class MoviespiderSpider(scrapy.Spider):
    # 设置爬虫名称,settings.py 配置文件中引用
    name = "moviespider"
    # 设置爬虫允许访问的网络域名范围
    #allowed_domains = ["douban.com"]
    # 设置爬虫可访问的网页列表,若有多个网页可以使用','逗号分隔
    #start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    # parse()函数作用:根据 XPath 规则检索需要采集的网页数据
    # response 参数为指定访问网页的 HTML 标签源代码
    def parse(self, response):
        # 获取当前页面中的电影信息标签<div class="item">并生成一个列表
        currentpage_movie_items = response.xpath('//div[@class="item"]')
        # 循环遍历电影信息列表
        for movie_item in currentpage_movie_items:
            # 创建一个 Movie 对象
            movie = MovieItem()
            # 获取电影排名并赋值 rank 属性
            movie['rank'] = movie_item.xpath('div[@class="pic"]/em/text()').extract()
            # 获取电影名称并赋值 title 属性
            movie['title'] = movie_item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            # 获取电影详情链接地址并赋值 link 属性
            movie['link'] = movie_item.xpath('div[@class="pic"]/a/@href').extract()
            # 获取电影评分并赋值 rating_属性
            movie['rating'] = movie_item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            # 获取电影参评人数并赋值 participants 属性
            movie['participants'] = movie_item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract()
            # 获取电影最新评论信息并赋值 quote 属性
            movie['quote'] = movie_item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # 将封装好的一个电影信息添加到容器中,yield 作用是创建一个列表并添加元素
            yield movie
