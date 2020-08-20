# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道文件，负责item后期处理或保存
class MyspiderPipeline(object):
    def __init__(self):  # 定义一些需要初始化的参数
        self.file = open('music.json', mode='a')


# 管道每次接受到item后执行方法
    def process_item(self, item, spider):
        print('---------------------------------------------', item)
        content = str(item) + '\n'
        self.file.write(content)  # 写入数据到本地
        return item

# 当爬取结束时执行的方法
    def close_spider(self, spider):
        self.spider.close()
        pass
