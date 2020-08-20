# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SunspiderPipeline(object):
    def __init__(self):
        self.filename = open('./sun.txt', mode='a', encoding='utf-8')
    def process_item(self, item, spider):
        # 构造每个写入的item
        content = str(item) + '\n\n'
        # 写入
        self.filename.write(content)

        return item

    def spider_close(self, spider):
        self.filename.close()
