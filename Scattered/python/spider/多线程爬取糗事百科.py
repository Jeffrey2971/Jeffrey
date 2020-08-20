import threading
import queue
import winreg
import time
import requests
from lxml import etree

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,  # 获取系统桌面地址
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
path = (winreg.QueryValueEx(key, "Desktop")[0])


class Thread1(threading.Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        try:
            while not flag_1:  # 处理网页
                print('线程启动！' + self.thread_name)
                page = self.page_queue.get()
                url = 'http://www.lovehhy.net/Joke/Detail/QSBK/' + str(page)
                connect = requests.get(url, headers=self.headers).text
                time.sleep(0.5)
                self.data_queue.put(connect)
        except Exception as error:
            print(error)
        print('线程结束！')


class Thread2(threading.Thread):  # 解析
    def __init__(self, thread_name, data_queue, file_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.file_name = file_name

    def run(self):
        try:
            while not flag_2:
                print('线程开始！' + self.thread_name)
                data = self.data_queue.get()
                html = etree.HTML(data)
                note_list = html.xpath('//div/h3[@class="red"]/a[@target="_blank"]')
                for note in note_list:
                    data_1 = note.text
                    self.file_name.write(data_1 + '\n')
        except Exception as error:
            print(error)
        print('线程结束！' + self.thread_name)


flag_1 = False
flag_2 = False

def main():
    pageQueue = queue.Queue(maxsize=3)
    for page in range(1, 4):
        pageQueue.put(page)

    data_queue = queue.Queue(maxsize=3)
    file_name = open(path + '\\1.txt', 'a')

    t1 = Thread1('采集线程！', pageQueue, data_queue)
    t1.start()
    t2 = Thread2('解析线程！', data_queue, file_name)
    t2.start()

    while not pageQueue.empty():
        pass
    global flag_1
    flag_1 = True

    while not data_queue.empty():
        pass
    global flag_2
    flag_2 = True

    t1.join()
    t2.join()

    file_name.close()
    print('执行完毕！')


if __name__ == '__main__':
    main()
