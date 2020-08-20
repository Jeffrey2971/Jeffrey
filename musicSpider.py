import requests
import time
import re
import os

'''
第一步url 分析

需要爬取网页第一页 Request URL: http://www.htqyy.com/top/hot
需要爬取网页第二页 Request URL: http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
需要怕取网页第三页 Request URL: http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
需要爬取网页第四页 Request URL: http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20
需要爬取网页第五页 Request URL: http://www.htqyy.com/top/musicList/hot?pageIndex=4&pageSize=20

分析结果：
1、此网站任何资源每天只允许下载两次(不计入分享等)
2、此音乐网没有任何反爬虫手段
3、首页地址(第一页)为Request URL: http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
4、pageIndex=后的数字为网页的第几页
5、pageSize=后的数字为每页的歌曲数量为20
6、主体链接为http://www.htqyy.com/top/musicList/hot?
7、每页中的包含每首歌曲的url类似为（歌曲url）Request URL: http://www.htqyy.com/play/22（清晨）
                                         Request URL: http://www.htqyy.com/play/62（月光下的凤尾竹）
                                         Request URL: http://www.htqyy.com/play/55（故乡的原风景）
8、               每首歌曲的真正的资源   Request URL: http://f2.htqyy.com/play7/261/mp3/12
9、每页返回的链接提取后每首歌曲的关键参数(title=, sid=)：
<span class="title"><a href="/play/61" target="play" title="雨的印记" sid="61">雨的印记</a></span>

'''


def _len(SongName, SongID):  # 此模块用来对比提取到的信息
    if not len(SongName) == len(SongID):
        print('提取到的信息不对成！')
        quit()
    return


def _enter(num):  # 此模块用于判断用户输入是否为数字
    if num == '':
        print('输入不能为空！')
        os.system('pause>nul')
        quit()
    result_type = num.isdigit()
    if result_type is False:
        print('只能输入 0-9 的数字！')
    return


def write(data,_time):  # 此模块用于写入文件到本地
    try:
        path = 'e:\\music'
        result_path = os.path.exists(path)
        if result_path is False:
            os.mkdir(path)
        print(type(id_list), '下载完成，正在保存：' + str(Song_name) + '\n----------------')
        with open(path + '\\{}.mp3'.format(Song_name), 'wb') as f:  # 打开通道并以二进制形式写入文件
            f.write(data)
        time.sleep(int(_time))
        return time
    except Exception as error:
        with open('e:\\music\\error.log', 'r') as r:
            r.write(str(error))
        print('下载成功了，但是保存时出现了异常' + '\nError：' + str(error))
        os.system('pause>nul')
        quit()


if __name__ == '__main__':

    beginPage = (input('请输入下载起始页：'))
    if beginPage == '0':
        print('请从第一页开始！')
        os.system('pause>nul')
        quit()
    _enter(beginPage)
    beginPage = int(beginPage)
    beginPage -= 1  # 首页页码为 0 所以用户输入第一页时需 1-1=0
    endPage = (input('请输入下载结束页：'))
    if endPage == '0':
        print('结束页不能为0')
        os.system('pause>nul')
        quit()
    _enter(endPage)
    endPage = int(endPage)
    _time = (input('请输入下载间隔时间(间隔时间如果断可能会被服务器检测为爬虫并终止你的链接一段时间，默认为两秒)：'))
    if _time == '':
        _time = str(2)
    _enter(_time)
    _time = int(_time)
    time_consuming = _time
    # ------------------------
    SongID = []  # 存放每首歌曲的sid号
    SongName = []  # 存放每首歌曲对应sid号的名字

    for i in range(beginPage, endPage):
        url = 'http://www.htqyy.com/top/musicList/hot?pageIndex=' + str(i) + '&pageSize=20'
        try:
            html = requests.get(url)  # 获取音乐榜单的网页信息
            _re = html.text

            pat_1 = r'sid="(.*?)"'  # 获取歌曲对应的sid
            pat_2 = r'title="(.*?)" sid'  # 获取歌曲对应的名字

            id_list = re.findall(pat_1, _re)  # 存放提取到的sid信息
            name_list = re.findall(pat_2, _re)  # 存放提取到的title信息(歌曲的名字)

            SongID.extend(id_list)  # 将所有获取到的sid信息合并到SongID
            SongName.extend(name_list)  # 将所有获取到的title信息合并到SongName
        except Exception as error:
            with open('e:\\music\\error.log', 'a') as r:
                r.write(str(error))
            print('连接异常！' + '\nError：' + str(error))
            os.system('pause>nul')
            quit()

    _len(SongID, SongName)

    for x in range(0, len(SongID)):
        try:
            Song_url = 'http://f2.htqyy.com/play7/' + str(SongID[x]) + '/mp3/12'
            Song_name = SongName[x]
            print('正在下载第' + str(x + 1) + '首歌' + '\n下载间隔为' + str(_time) + '秒，已耗时' + str(time_consuming) + '秒\n歌名为：' + Song_name + '\n----------------')
            data = requests.get(Song_url).content
            write(data, _time)
            time_consuming += _time
        except Exception as error:
            with open('e:\\music\\error.log', 'a') as r:
                r.write(str(error))
            print('下载异常！' + '\nError：' + str(error))
            os.system('pause>nul')
            quit()

    print('下载完成，总共下载了' + str(x+1) + '首歌，耗时' + str(time_consuming) + '秒')
print('运行结束，按任意键退出！')
os.system('pause>nul')
