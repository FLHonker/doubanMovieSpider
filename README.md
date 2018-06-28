# 基于Scrapy爬虫框架的douban电影top250


### v1.0 日志:

1. 添加了pipelines2excel模块,将爬取到的数据导出到excel表格;
2. 添加rotate_useragent 浏览器代理模块,防止网站进制访问,此模块在其他爬虫项目中亦可复用;
3. 添加爬取电影海报链接地址