# -*- coding: utf-8 -*-
import scrapy


class FanyispiderSpider(scrapy.Spider):
    name = 'fanyispider'
    allowed_domains = ['fanyi.youdao.com']
    # start_urls = ['http://fanyi.youdao.com/']

    def start_requests(self):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        # 向队列中加入一个带有表单信息的post请求
        yield scrapy.FromRequest(
        url=url,
            fromdata={
                        'i': '北京',
                         'from': 'AUTO',
                         'to': 'AUTO',
                         'smartresult': 'dict',
                         'client': 'fanyideskweb',
                         'salt': '15764179485786',
                         'sign': 'bbe247ed7b1fd652524877b91c20521a',
                         'ts': '1576417948578',
                         'bv': '1737e427',
                         'doctype': 'json',
                         'version': '2.1',
                         'keyfrom': 'fanyi.web',
                         'action': 'FY_BY_REALTlME'
            },
            callback=self.parse





        )


    def parse(self, response):
        pass
