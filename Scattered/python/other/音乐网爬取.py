import requests
import time
import re
'''

url规律分析

# http://www.htqyy.com/top/hot 榜单第一页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20  榜单第二页
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20  榜单第三页
# http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20  榜单第四页

# 经分析 PageIndex为页码 pageSize为每页的歌曲数量
# 第一页为 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20

'''

# 页码 -1
# 歌曲url http://www.htqyy.com/play/33 第一页第一首
# 歌曲url http://www.htqyy.com/play/61 第二页第一首
# 歌曲资源所在url http://f2.htqyy.com/play7/61/mp3/12
songID = []
songName = []

for i in range(0, 2):
    url = 'http://www.htqyy.com/top/musicList/hot?pageIndex=' + str(i) + '&pageSize=20'
    # 获取音乐榜单的网页信息
    html = requests.get(url)

    pat_1 = r'title="(.*?)" sid'
    pat_2 = r'sid="(.*?)"'

    strr = html.text

    id_list = re.findall(pat_2, strr)
    title_list = re.findall(pat_1, strr)

    songID.extend(id_list)
    songName.extend(title_list)
# span class="title"><a href="/play/62" target="play" title="月光下的凤尾竹" sid="62">月光下的凤尾竹</a></span>

print(len(songID))
print(len(songName))

for i in range(0, len(songID)):
    songurl = 'http://f2.htqyy.com/play7/' + str(songID[i]) + '/mp3/12'
    songname = songName[i]

    data = requests.get(songurl).content

    print('正在下载第'+str(i)+'首')

    with open('e:\\music\\{}.mp3'.format(songname), 'wb') as f:
        f.write(data)
