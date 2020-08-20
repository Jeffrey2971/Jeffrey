# -*- coding: utf-8 -*-
from mySpider.items import MyspiderItem
import scrapy
import re

class MusicspiderSpider(scrapy.Spider):
    name = 'musicSpider'  # 爬虫识别名称
    allowed_domains = ['htqyy.com']  # 爬取的网页范围
    start_urls = ['http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20']  # 起始url

    def parse(self, response):
        # filename = 'music.html'
        data = response.body.decode()  # 获取响应内容
        # open(filename, mode='wb').write(data)  # 写入到本地

        # items = []  # 存放音乐信息

        titles = re.findall(r'title="(.*?)" sid', data)
        artists = re.findall(r'target="_blank">(.*?)</a>', data)

        for i in range(0, len(titles)):
            item = MyspiderItem()

            item['title'] = titles[i]
            item['artist'] = artists[i]
            yield item
        #     items.append(item)
        # return items

            # 获取当前请求的url，提取出页码信息
            beforeurl = response.url  # 上一次url
            page = re.search(r'pageIndex=(\d)', beforeurl).group(1)

            page = int(page) + 1  # 得到下一次请求pageIndex信息

            if page < 5:  # 爬取前五页
                next_url = 'http://www.htqyy.com/top/musicList/hot?pageIndex=' + str(page) + '&pageSize=20'
                # 发送下一次请求
                yield scrapy.Request(next_url, callback=self.parse)  # 在parse方法里请求，并且这个请求完成后会调用parse方法

            # 构造下一页的url，发送下一次请求