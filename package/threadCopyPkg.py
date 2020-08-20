#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 上午3:30
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : threadCopyPkg.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

import os
import queue
import shutil
import threading
import time


class indexError(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return self.error_info


class index(object):
    """
    需提供三个必要参数，一个可选参数
    @work_path：程序工作路径
    @save_path：程序的保存路径
    @file_type：指定一个筛选文件类型
    @move_default：是否移动，默认为否
    """

    def __init__(self, work_path, save_path, file_type, move_default=False):
        self.workPath = work_path
        self.savePath = save_path
        self.fileType = file_type
        self.moveDefault = move_default
        begin = time.time()

        if self.workPath == "":
            error = "请提供一个的工作路径"
            raise indexError(error)
        elif not os.path.exists(self.workPath):
            error = ("%s不是一个有效的工作路径" % self.workPath)
            raise indexError(error)
        if self.savePath == "":
            error = "请提供一个保存路径"
            raise indexError(error)
        elif not os.path.exists(self.savePath):
            error = "%s不是一个有效的保存路径" % self.savePath
            raise indexError(error)

        if self.fileType == "":
            error = "请填写需操作的文件类型"
            raise indexError(error)

        run(self.workPath, self.savePath, self.fileType, self.moveDefault, begin)


"""global finish --> 解决采集线程的速度跟不上复制线程而break"""
thread_1 = False


class Thread1(threading.Thread):
    def __init__(self, work_path, file_type, data_queue):
        threading.Thread.__init__(self)
        self.workPath = work_path
        self.fileType = file_type
        self.dataQueue = data_queue

    def run(self):
        findNum = 0  # 找到的文件
        lostNum = 0  # 丢弃的文件
        while True:
            try:
                for home, dirs, files in os.walk(self.workPath):
                    for filename in files:
                        path = os.path.join(home, filename)
                        if path.endswith(self.fileType):
                            self.dataQueue.put(path)
                            findNum += 1
                            print("已找到" + str(findNum) + "个文件")
                        else:
                            lostNum += 1
                            print("已过滤" + str(lostNum) + "个文件")
                print("-------------------------------------------------------------")
                print("共找到" + str(findNum) + "个文件，过滤了" + str(lostNum) + "个文件")
                global thread_1
                finish = True  # 需声明采集已经结束
                print("1")
                print("结束线程：", threading.current_thread())
                break  # 找的速度跟不上取的速度会发生异常
            except Exception as e:
                error = "发生错误%s" % e
                raise indexError(error)


class Thread2(threading.Thread):
    def __init__(self, data_queue, save_path, default_move, begin):
        threading.Thread.__init__(self)
        self.dataQueue = data_queue
        self.savePath = save_path
        self.defaultMove = default_move
        self.beginTime = begin

    def run(self):
        num = 0  # 移动或复制
        size_all = 0  # 计算文件大小
        while True:
            print("线程2执行ing")
            try:
                if self.dataQueue.empty() and thread_1 is True:
                    endTime = time.time()
                    if self.defaultMove is True:
                        mode = "移动"
                    else:
                        mode = "复制"
                    sizeGB = "%.2f" % (size_all / 1024 / 1024 / 1024)
                    sizeMB = "%.2f" % (size_all / 1024 / 1024)
                    total = "%.2f" % (endTime - self.beginTime)
                    minute = float(total) / 60
                    if minute < 1:
                        minute = 0
                    print("-------------------------------------------------------------")
                    print(
                        "已完成，共" + mode + "了" + str(num) + "个文件，总大小为" + sizeGB + "GB，" + sizeMB + "MB，" + "耗时" + str(
                            minute) + "分" + str(
                            total) + "秒")
                    print("2")
                    print("结束线程：", threading.current_thread())
                    global thread2
                    thread2 = True
                    break
                elif not self.dataQueue.empty():  # 假如不为空
                    print("取值ing")
                    """如果dataQueue没有值，执行取值操作会卡死且不报错"""
                    file = self.dataQueue.get()
                    size_all += os.path.getsize(file)
                    if self.defaultMove is True:
                        shutil.move(file, self.savePath)
                        num += 1
                        print("已移动" + str(num) + "个文件：" + file)
                    else:
                        shutil.copy(file, self.savePath)
                        num += 1
                        print("已复制" + str(num) + "个文件：" + file)

            except Exception as e:
                error = "发生错误%s" % e
                raise indexError(error)


def run(work_path, save_path, file_type, move_default, begin):
    try:
        dataQueue = queue.Queue()
        T1 = Thread1(work_path, file_type, dataQueue)
        T2 = Thread2(dataQueue, save_path, move_default, begin)
        T1.start()
        T2.start()

        while True:
            if dataQueue.empty() is True and thread_1 is True:
                print("程序退出", threading.current_thread())
                break

    except Exception as e:
        error = "发生错误%s" % e
        raise indexError(error)
