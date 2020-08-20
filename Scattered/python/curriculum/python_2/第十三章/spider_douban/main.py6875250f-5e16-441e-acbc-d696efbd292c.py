# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/15 08:45
# @Author  : lemon

import requests
from lxml.html import fromstring
import json


class SpiderDouban():
    def __init__(self,url):
        self.url = url
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/cinema/nowplaying/guangzhou/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }

    def get_data(self):
        r = requests.get(url=self.url,headers = self.headers)

        data = fromstring(r.text)

        selector = data.xpath('//div[@id="nowplaying"]/div[@class="mod-bd"]/ul/li')

        movie_data = []

        for i in selector:
            title = i.xpath('@data-title')[0]
            score = i.xpath('@data-score')[0]
            votecount = i.xpath('@data-votecount')[0]
            duration = i.xpath('@data-duration')[0]
            release = i.xpath('@data-release')[0]
            region = i.xpath('@data-region')[0]
            director = i.xpath('@data-director')[0]
            actors = i.xpath('@data-actors')[0]

            movie_data.append({
                'title': title if title else '',
                'score': score if score else '',
                'votecount': votecount if votecount else '',
                'duration': duration if duration else '',
                'release': release if release else '',
                'region': region if region else '',
                'director': director if director else '',
                'actors': actors if actors else '',


            })

        with open('files/movie_data.json','w',encoding='utf-8') as f:
            json.dump(movie_data,f,indent=1,ensure_ascii=False)

        pass




if __name__ == '__main__':
    s = SpiderDouban('https://movie.douban.com/cinema/nowplaying/guangzhou/')
    s.get_data()




