# 多线程练习，没什么卵用
import threading
import queue
import requests
import datetime
import re
from fake_useragent import UserAgent
from lxml import etree


class Thread1(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.min_url = r'http://www.themesmap.com/theme.html?t=time&page='
        self.logPath = r'/home/jeffrey/package/report.log'

    def run(self):
        print(self.threadName)
        while not flag_Thread1:
            try:
                a_g = UserAgent()
                page = self.pageQueue.get()
                url = self.min_url + str(page)
                data = requests.get(url=url, headers={"User-Agent": a_g.random}).text
                self.dataQueue.put(data)
            except BaseException as e:
                global items
                items += 1
                exhibition = ('采集线程出现了一个错误：', e)
                with open(self.logPath, mode='a') as f:
                    f.write(str(exhibition) + '\n\n')
                    print(exhibition)
            finally:
                pass


class Thread2(threading.Thread):
    def __init__(self, threadName, dataQueue, urlQueue, titleQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.urlQueue = urlQueue
        self.titleQueue = titleQueue
        self.min_url = r'http://www.themesmap.com/'
        self.logPath = r'/home/jeffrey/package/report.log'

    def run(self):
        print(self.threadName)
        while not flag_Thread2:
            try:
                data = self.dataQueue.get()
                # print(data)
                html_page = etree.HTML(data)
                xpath_theme = html_page.xpath('//div[@class="row"]/div[@class="col"]/a/@href')
                xpath_title = html_page.xpath('//div[@class="col"]/a[@class="card"]/h2[@class="card-header"]/text()')

                if len(xpath_theme) == len(xpath_title):
                    # print(len(xpath_theme), len(xpath_title))
                    for theme, title in zip(xpath_theme, xpath_title):
                        # self.min_url + theme
                        a_g = UserAgent()
                        content = requests.get(url=self.min_url + theme, headers={"User-Agent": a_g.random}).text
                        html_theme = etree.HTML(content)
                        down_url = self.min_url + html_theme.xpath('//div[@class="content-th-info"]/a/@href')[0]
                        self.urlQueue.put(down_url)
                        self.titleQueue.put(title)
                else:
                    print('信息不对称')

            except BaseException as e:
                global items
                items += 1
                exhibition = ('解析线程时出现了一个错误：', e)
                with open(self.logPath, mode='a') as f:
                    f.write(str(exhibition) + '\n\n')
                    print(exhibition)
            finally:
                pass


class Thread3(threading.Thread):
    def __init__(self, threadName, urlQueue, titleQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.urlQueue = urlQueue
        self.titleQueue = titleQueue
        self.path = r'/home/jeffrey/theme'
        self.logPath = r'/home/jeffrey/package/report.log'

    def run(self):
        print(self.threadName)
        while not flag_Thread3:
            try:
                # print(self.urlQueue.get())
                # print(self.titleQueue.get())
                a_g = UserAgent()
                data = requests.get(url=self.urlQueue.get(), headers={"User-Agent": a_g.random}).content
                title = self.titleQueue.get()
                check_list = ['/', '\\', ':', '|', '*', '<', '>', '?', '"']
                if any(key in title for key in check_list):
                    title = check(title)
                else:
                    exhibition = '当前网站共', page, '页，约', int(page) * 12, '个主题，正在下载', title + '.jar'
                    with open(self.logPath, mode='a', encoding='utf-8') as f:
                        f.write(str(exhibition) + '\n\n')
                        print(exhibition)
                    with open(self.path + '\\{}.jar'.format(title), mode='wb') as f:
                        f.write(data)
                        global num
                        num += 1
            except BaseException as e:
                global items
                items += 1
                exhibition = ('下载线程时出现了一个错误：', e)
                with open(self.logPath, mode='a') as f:
                    f.write(str(exhibition) + '\n\n')
                    print(exhibition)
            finally:
                pass


logPath = r'/home/jeffrey/package/report.log'
flag_Thread1, flag_Thread2, flag_Thread3 = False, False, False
num, items = 0, 0


def check(change):
    pattern = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    title = re.sub(pattern, "_", change)  # 替换为下划线
    exhibition = ('发现非法命名', change, '已更改为', title)
    with open(logPath, mode='a') as f:
        f.write(str(exhibition) + '\n\n')
        print(exhibition)
    return title


def main(max_page):
    # print(type(max_page))-str
    print('主线程启动')
    try:
        start_time = datetime.datetime.now()
        pageQueue, dataQueue, urlQueue, titleQueue = queue.Queue(), queue.Queue(), queue.Queue(), queue.Queue()
        for page in range(int(1), int(max_page) + 1):
            pageQueue.put(page)

        T1 = Thread1("采集线程启动", pageQueue, dataQueue)
        T2 = Thread2("解析线程启动", dataQueue, urlQueue, titleQueue)
        T3 = Thread3("下载线程启动", urlQueue, titleQueue)

        T1.start()
        T2.start()
        T3.start()

        while not pageQueue.empty():
            pass
        global flag_Thread1
        flag_Thread1 = True
        print('----------\n' + '采集线程结束\n' + '----------')

        while not dataQueue.empty():
            pass
        global flag_Thread2
        flag_Thread2 = True
        print('----------\n' + '解析线程结束\n' + '----------')

        while not urlQueue.empty():
            pass
        global flag_Thread3
        flag_Thread3 = True
        print('----------\n' + '下载线程结束\n' + '----------')

        T1.join()
        T2.join()
        T3.join()

        exhibition = '爬取完毕，共下载了', num, '个主题，发生了', items, '个线程异常，总耗时', start_time - datetime.datetime.now()

        with open(logPath, mode='a') as f:
            f.write(str(exhibition) + '\n\n')
            print(exhibition)

    except BaseException as e:
        exhibition = ('某些问题使爬虫终止了运行：', e)
        with open(logPath, mode='a') as f:
            f.write(str(exhibition) + '\n\n')


if __name__ == '__main__':
    try:
        a_g = UserAgent()
        url = r'http://www.themesmap.com/theme.html'
        data_ = requests.get(url=url, headers={"User-Agent": a_g.random}).text
        html = etree.HTML(data_)
        max_page = html.xpath(
            '//div[@class="pagination_text"]/ul[@class="pagination"]//li[@class="footable-page-arrow"]/a/@href')[2]
        pattern_max_page = re.compile(r'\d+')
        page = pattern_max_page.findall(max_page)[0]
        main(page)
    except BaseException as e:
        exhibition = ('获取最大页码时发生了错误使爬虫无法继续', e)
        with open(logPath, mode='a') as f:
            f.write(str(exhibition) + '\n\n')
            print(exhibition)
