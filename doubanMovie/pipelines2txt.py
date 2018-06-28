# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
# 设置字符集变量default_encoding为utf-8
default_encoding = 'utf-8'
# 判断系统当前默认字符是否为指定的utf-8
if sys.getdefaultencoding() != default_encoding:
    # 使用reload()函数重新加载sys模块
    reload(sys)
    # 设置系统默认字符集为utf-8
    sys.setdefaultencoding(default_encoding)
import  os
import  time

class DoubanmoviePipeline(object):
    def __init__(self):
        #创建文件夹output
        self.folder_name='../data'
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
            pass
    def process_item(self, item, spider):
        currentTime=time.strftime('%Y-%m-%d',time.localtime())
        fileName='top250-'+currentTime+'.txt'
        try:
            with open(self.folder_name+'/'+fileName,'a') as fp:
                fp.write(u'排名:'+item['rank'][0]+'\n')
                fp.write(u'电影名称:'+item['title'][0]+'\n')
                fp.write(u'海报地址:'+item['pic_url'][0]+'\n')
                fp.write(u'详情链接:'+item['link'][0]+'\n')
                fp.write(u'评分:'+item['rating'][0]+'\n')
                fp.write(u'参评人数:'+item['participants'][0]+'\n')
                fp.write(u'最新评论:'+item['quote'][0]+'\n\n')
                pass
        except EOFError as er:
            print er
        finally:
            #关闭文件指针
            fp.close()
        return item
