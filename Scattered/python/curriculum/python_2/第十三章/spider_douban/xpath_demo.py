# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/17 10:18
# @Author  : lemon

from lxml.html import fromstring

with open('files/index.html','r',encoding='utf-8') as f:
    data = f.read()


selector = fromstring(data)

h1 = selector.xpath('//h1/text()')[0]
p  = selector.xpath('//body/p/text()')[0]

div_ul = selector.xpath('//div/ul/text()')

# div_p  = selector.xpath('//div[@id="list"]/p/text()')
div_p  = selector.xpath('//div[@id="list"]/p[@class="Hadoop"]/text()')

pass



