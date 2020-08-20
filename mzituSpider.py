#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 下午2:12
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : mzituSpider.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

import requests
from lxml import etree
from fake_useragent import UserAgent
import threading
import queue
import datetime


class Thread1(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        threading.Thread.__init__(self)
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.threadName = threadName
        self.min_url = r'https://www.mzitu.com/page/'
        self.error_path = errorLogPath

    def run(self):
        print(self.threadName)
        while not flag_Thread1:
            try:
                page = self.pageQueue.get()
                url = self.min_url + str(page) + '/'
                Agent = UserAgent()
                header = {"User-Agent": Agent.random, "referer": "https://www.mzitu.com/"}  # 需加上referer
                data = requests.get(url=url, headers=header).text
                self.dataQueue.put(data)
            except BaseException as e:
                global error_times
                error_times += 1
                try:
                    et = datetime.datetime.now()
                    with open(self.error_path, mode='a') as f:
                        f.write(str(et) + '：' + str(e) + '\n\n')
                    print('采集线程时出现了一个错误，已写入报告', self.error_path)
                except Exception as e:
                    print('采集线程时出现了一个错误，写入报告时发生了错误', e)


class Thread2(threading.Thread):
    def __init__(self, threadName, dataQueue):
        threading.Thread.__init__(self)
        self.dataQueue = dataQueue
        self.threadName = threadName
        self.path = savePath
        self.error_path = errorLogPath

    def run(self):
        print(self.threadName)
        while not flag_Thread2:
            try:
                page_data = self.dataQueue.get()
                html = etree.HTML(page_data)
                pattern_img = html.xpath('//ul[@id="pins"]/li/a/img[@class="lazy"]/@data-original')
                pattern_title = html.xpath('//div[@class="postlist"]/ul[@id="pins"]//li/span/a/text()')
                Agent = UserAgent()
                header = {"User-Agent": Agent.random, "referer": "https://www.mzitu.com/"}  # 需加上referer
                # print(pattern)

                for img, title in zip(pattern_img, pattern_title):
                    data = requests.get(url=img, headers=header).content
                    with open(self.path + '//{}.jpg'.format(title), mode='wb') as f:
                        f.write(data)
                        global num
                        num += 1
                        print('当前网站总共为', max_page, '页，', '约', int(max_page)*24, '张图片，', '已下载', num, '张')

            except BaseException as e:
                global error_times
                error_times += 1
                try:
                    et = datetime.datetime.now()
                    with open(self.error_path, mode='a') as f:
                        f.write(str(et) + '：' + str(e) + '\n\n')
                        print('解析或下载时出现了一个错误，已写入报告', self.error_path)
                except Exception as e:
                    print('解析或下载时出现了一个错误，写入报告时发生了错误', e)


flag_Thread1, flag_Thread2, error_times, num = False, False, 0, 0


def main():
        """
       
    
        """
        try:
            print('主线程启动')
            # headers
            Agent = UserAgent()
            header = {"User-Agent": Agent.random, "referer": "https://www.mzitu.com/"}  # 需加上referer
            data = requests.get(url='https://www.mzitu.com/page/1/', headers=header).text
            html = etree.HTML(data)
            global max_page
            max_page = html.xpath('//div[@class="nav-links"]/a[@class="page-numbers"]/text()')[3]
            # print(max_page)
            pageQueue = queue.Queue()
            dataQueue = queue.Queue()
            for page in range(1, int(max_page) + int(1)):
                pageQueue.put(page)

            T1 = Thread1('采集线程启动', pageQueue, dataQueue)
            T2 = Thread2('解析线程启动', dataQueue)
            T1.start()
            T2.start()
    
            while not pageQueue.empty():
                pass  # 堵塞主线程直到队列中的值被取完
            global flag_Thread1
            flag_Thread1 = True

            while not dataQueue.empty():
                pass  # 堵塞主线程直到队列中的值被取完
            global flag_Thread2
            flag_Thread2 = True

            T1.join()
            T2.join()
            print('爬取完毕，总共下载了', num, '张图片，发生了', error_times, '个异常')
        except BaseException as e:
            try:
                et = datetime.datetime.now()
                error_path = errorLogPath
                with open(error_path, mode='a') as f:
                    f.write(str(et) + '：' + str(e) + '\n\n')
                    print('出现了某些错误使爬虫终止运行，错误已写入报告', error_path)
            except Exception as e:
                print('出现了某些错误使爬虫终止运行，写入报告时发生了错误', e)


if __name__ == '__main__':
    # 错误报告存放路径
    errorLogPath = ""
    # 文件保存位置
    savePath = "/Users/jeffrey/Desktop/test"
    main()
    

