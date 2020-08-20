# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/11 14:33
# @Author  : lemon


import json
import requests
from lxml.html import fromstring


def get_title(url):
    headers = {
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/cinema/nowplaying/guangzhou/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
    }

    r = requests.get(url,headers=headers)

    if not r.status_code == 200:
        return ''

    data = fromstring(r.text)
    movie_list  = data.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li')
    movie_message = []

    for i in movie_list:
        title = i.xpath('@data-title')[0]
        score = i.xpath('@data-score')[0]
        votecount = i.xpath('@data-votecount')[0]
        duration = i.xpath('@data-duration')[0]
        release =  i.xpath('@data-release')[0]
        region = i.xpath('@data-region')[0]
        director = i.xpath('@data-director')[0]
        actors = i.xpath('@data-actors')[0]
        showed = i.xpath('@data-showed')[0]

        movie_message.append({
            '电影名称':title if title else '',
            '电影评分':score if score else '',
            '电影评分人数':votecount if votecount else '',
            '电影时长':duration if duration else '',
            '上映年份':release if release else '',
            '地区':region if  region else '',
            '导演':director if  director else '',
            '主要演员': actors if actors else '',
            '正在上映': showed if showed else ''
        })

    with open('../files/movie.json','w',encoding='utf-8') as f:
        json.dump(movie_message,f,ensure_ascii=False,indent=1)



if __name__ == '__main__':
    get_title('https://movie.douban.com/cinema/nowplaying/guangzhou/')


