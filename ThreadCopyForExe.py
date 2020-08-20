# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午2:39
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : ThreadCopyBeta.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

"""2020-6-21已归档不再更新"""
"""脚本版"""

import datetime
import hashlib
import os
import queue
import re
import sys
import threading
import shutil
import time
import uuid
import math

"""global finish1 --> 解决采集线程的速度跟不上复制线程而break"""
thread_1 = False
# thread_2 = False
# thread_3 = False
out = False


class indexError(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        global out
        out = True
        return self.error_info


def debug(data):
    with open("/Users/jeffrey/test/debug/debug.log", mode="a") as d:
        d.write("##########################################" + "\n")
        d.write("时间：" + str(datetime.datetime.now()) + "\n")
        d.write("信息：" + "\n")
        d.write(data)
        d.write("\n" + "##########################################")


def write_md5(file, path):
    with open(file, mode="rb") as f:
        md5 = str(hashlib.md5(f.read()).hexdigest())
        with open(path + os.sep + "md5.log", mode="a") as m:
            m.write(md5 + "\n")


def field_error(data):
    print(data)
    os.system("pause")
    exit()


"""Thread1负责采集资源"""


class Thread1(threading.Thread):
    def __init__(self, work_path, file_type, save_path, data_queue, wait_queue, backups_default, old_list):
        threading.Thread.__init__(self)
        self.workPath = work_path  # 工作路径，用于指定筛选的路径 str
        self.savePath = save_path  # 保存路径，用于找到文件后保存的目录 str
        self.fileType = file_type  # 文件类型，用于索引指定的文件 list
        self.dataQueue = data_queue  # 找到的文件 queue
        self.waitQueue = wait_queue  # 重名文件 queue
        self.default = backups_default  # 指定的md5文件是否合法 boolean
        self.checkList = []  # 存放所找到的文件名称(不包含路径)，用于判断是否文件名重复 list
        self.fileTypeTmp = []  # 存放类型文件的临时列表 list
        self.oldMd5List = old_list  # 存放读取到md5文件的列表 list

    def run(self):
        findNum = 0  # 找到的文件
        global lostNum
        lostNum = 0  # 丢弃的文件
        for x in self.fileType:
            self.fileTypeTmp.append(x)
        while True:
            try:
                if len(self.fileTypeTmp) != 0:
                    for w in self.fileTypeTmp.copy():
                        for home, dirs, files in os.walk(self.workPath):
                            # """计算相差百分比，处理较大类型文件时可暂时睡眠采集线程，将更多的资源留给线程2"""
                            # if findNum != 0 and not self.numQueue.empty():
                            #     if int(("%.0f" % (float(findNum) / float(self.numQueue.qsize())))) > 40:
                            #         print(threading.current_thread().getName() + "等待")
                            #         time.sleep(60)

                            for filename in files:
                                path = os.path.join(home, filename)
                                if os.path.splitext(path)[-1].replace(".", "") in self.fileType:
                                    with open(path, mode="rb") as f:
                                        md5 = str(hashlib.md5(f.read()).hexdigest())
                                    if self.default:
                                        if md5 not in self.oldMd5List:
                                            if path.split(os.sep)[-1] not in self.checkList:
                                                self.dataQueue.put(path)
                                                self.checkList.append(path.split(os.sep)[-1])  # 文件名.后缀名
                                            else:
                                                self.waitQueue.put(path)
                                            findNum += 1
                                            print(threading.current_thread().getName() + "：已找到" + str(
                                                findNum) + "个文件")
                                        else:
                                            """跳过"""
                                            pass
                                    else:

                                        if path.split(os.sep)[-1] not in self.checkList:
                                            self.dataQueue.put(path)
                                            self.checkList.append(path.split(os.sep)[-1])  # 文件名.后缀名
                                        else:
                                            self.waitQueue.put(path)
                                        findNum += 1
                                        print(threading.current_thread().getName() + "：已找到" + str(findNum) + "个文件")
                                else:
                                    lostNum += 1
                                    print(threading.current_thread().getName() + "：已过滤" + str(lostNum) + "个文件")

                        self.fileTypeTmp.remove(w)
                print("-------------------------------------------------------------")
                print("共找到" + str(findNum) + "个文件，过滤了" + str(lostNum) + "个文件")
                global thread_1
                thread_1 = True  # 需声明采集已经结束
                print("结束线程：", threading.current_thread())
                break  # 找的速度跟不上取的速度会发生异常
            except Exception as e:
                error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                # raise indexError(error)
                field_error(error)


"""Thread2负责复制或移动文件"""


class Thread2(threading.Thread):

    def __init__(self, data_queue, save_path, file_type, begin, wait_queue, thread_error, num_queue):
        threading.Thread.__init__(self)
        self.dataQueue = data_queue
        self.savePath = save_path
        self.fileType = file_type
        self.beginTime = begin
        self.waitQueue = wait_queue
        self.threadError = thread_error
        self.numQueue = num_queue
        # self.moveQueue = move_queue
        self.num = 0
        self.rename = 0

    def run(self):
        global file
        size_all = 0  # 计算文件大小
        while True:
            try:
                if self.dataQueue.empty() and thread_1 is True:
                    """处理重名文件"""
                    if self.waitQueue != 0:
                        """重名文件队列"""
                        path = self.waitQueue.get()
                        """计算文件的md5值并写入到文件中"""
                        write_md5(path, self.savePath)
                        """End"""

                        print("正在处理重名文件" + path + '\n' + "剩余" + str(self.waitQueue.qsize()))
                        self.rename += 1
                        try:
                            if move_default is True:
                                shutil.move(path,
                                            self.savePath + os.sep + path.split(os.sep)[-1] + "." + str(
                                                uuid.uuid4()) + "." +
                                            path.split(".")[-1])
                                # self.moveQueue.put(i)
                                self.num += 1
                                self.numQueue.put(self.num)
                                # self.numQueue.put(self.num)
                                print("已移动" + str(self.num) + "个文件：" + path)
                            else:
                                shutil.copyfile(path,
                                                self.savePath + os.sep + path.split(os.sep)[-1] + "." + str(
                                                    uuid.uuid4()) + "." +
                                                path.split(".")[-1])
                                # self.moveQueue.put(i)
                                self.num += 1
                                self.numQueue.put(self.num)
                                print("已复制" + str(self.num) + "个文件：" + path)
                        except Exception as e:
                            error = """
                            异常报告：
                            所在线程：%s
                            异常文件：%s
                            发现异常：%s
                            """ % (threading.current_thread().getName(), path, e)
                            self.threadError.append(error)

                    for L in self.fileType:
                        for w in os.listdir(self.savePath):
                            if w.endswith(L):
                                shutil.move(self.savePath + os.sep + w, self.savePath + os.sep + L)
                                print("正在处理类型文件：" + self.savePath + os.sep + w)

                    endTime = time.time()
                    if move_default is True:
                        mode = "移动"
                    else:
                        mode = "复制"
                    """处理类型文件"""
                    sizeGB = "%.2f" % (size_all / 1024 / 1024 / 1024)
                    sizeMB = "%.2f" % (size_all / 1024 / 1024)
                    total = "%.2f" % (endTime - self.beginTime)
                    minute = float(total) / 60
                    if minute < 1:
                        minute = 0
                    print("-------------------------------------------------------------")
                    global result
                    result = ("已完成，共" + mode + "了" + str(self.num) + "个文件，处理了" + str(self.rename) + "个重名文件，发生了" + str(
                        len(self.threadError)) + "个异常，忽略了" + str(
                        lostNum) + "个文件，总大小为" + sizeGB + "GB，" + sizeMB + "MB，" + "耗时" + str(
                        math.floor(minute)) + "分" + str(total) + "秒")
                    print(result)
                    print("结束线程：", threading.current_thread())

                    break

                if not self.dataQueue.empty():  # 假如不为空
                    try:
                        """如果dataQueue没有值，执行取值操作会卡死且不报错"""
                        """不重名的文件队列"""
                        file = self.dataQueue.get()
                        """计算文件的md5值并写入到文件中"""
                        write_md5(file, self.savePath)
                        """End"""

                        size_all += os.path.getsize(file)
                        if move_default is True:
                            shutil.move(file, self.savePath)
                            # self.moveQueue.put(file)
                            self.num += 1
                            self.numQueue.put(self.num)
                            print(threading.current_thread().getName() + "：已移动" + str(self.num) + "个文件：" + file)
                        else:
                            shutil.copy(file, self.savePath)
                            # self.moveQueue.put(file)
                            self.num += 1
                            self.numQueue.put(self.num)
                            print(threading.current_thread().getName() + "：已复制" + str(self.num) + "个文件：" + file)

                    except Exception as e:
                        error = """
                            异常报告：
                            所在线程：%s
                            异常文件：%s
                            发现异常：%s
                            """ % (threading.current_thread().getName(), file, e)
                        self.threadError.append(error)

            except Exception as e:
                error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                # raise indexError(error)
                field_error(error)


def run(work_path, save_path, md5_path, file_type, backups_default, begin):
    try:
        """尝试解决内存溢出"""
        sys.setrecursionlimit(1000000)

        """检查输入路径默认"""
        if work_path[-1] == os.sep:
            work_path = work_path.replace(work_path[-1], "")
        elif save_path[-1] == os.sep:
            save_path = save_path.replace(save_path[-1], "")

        """创建时间文件夹"""
        directory = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.mkdir(save_path + os.sep + str(directory))
        save_path = save_path + os.sep + str(directory)

        """创建类型文件夹"""
        for L in file_type:
            if not os.path.exists(save_path + os.sep + L):
                os.mkdir(save_path + os.sep + L)

        """判断读取md5文件"""
        oldMd5List = []
        if backups_default:
            if os.path.exists(md5_path):
                """读取提供的md5文件"""
                with open(md5_path, mode="r") as m:
                    for i in m:
                        oldMd5List.append(i.replace("\n", ""))

        """创建队列和列表供全局使用"""
        numQueue = queue.Queue()
        dataQueue = queue.Queue()
        waitQueue = queue.Queue()
        threadError = []
        # md5_queue = queue.Queue()
        # moveQueue = queue.Queue()
        # waitList = []

        """
        这里一定要使用队列存放重名文件而不是列表，否则会发生多次给同一个文件添加uuid值
        同一个工作目录下测试结果：
        正常：使用WaitQueue存放重名文件：已完成，共复制了81个文件，处理了1个重名文件，发生了0个异常，忽略了95010个文件，总大小为0.26GB，266.50MB，耗时0分31.52秒
        异常：使用WaitList存放重名文件：已完成，共复制了525个文件，忽略了95010个文件，总大小为0.26GB，266.50MB，耗时1分118.15秒
        """

        """创建并启动线程传递相关参数"""
        T1 = Thread1(work_path, file_type, save_path, dataQueue, waitQueue, backups_default, oldMd5List)
        T2 = Thread2(dataQueue, save_path, file_type, begin, waitQueue, threadError, numQueue)
        # T3 = Thread3(allQueue, save_path)
        T1.start()
        T2.start()
        # T3.start()

        """逻辑堵塞主线程"""
        while True:
            print("wait")
            if True:
                print("程序异常将终止！")
                exit()
            if dataQueue.empty() and thread_1:
                T1.join()
                T2.join()

                with open(save_path + os.sep + "md5.log", mode='r+') as tips:
                    content = tips.read()
                    tips.seek(0, 0)
                    tips.write(
                        "这个备份文件创建于：" + str(datetime.datetime.now()) + "，为了确保下次备份的正确性，请不要修改以下的内容" + "\n\n" + content)

                try:
                    """创建日志报告信息"""
                    with open(save_path + os.sep + "report.log", mode="a") as f:
                        for e in threadError:
                            f.write("------错误报告------" + '\n' + e + '\n')
                        f.write("------其他信息------" + '\n' + result + '\n')
                    print("已生成日志：" + save_path + os.sep + "report.log")
                except Exception as e:
                    print("生成日志失败：", e)
                # T3.join()
                print("程序退出", threading.current_thread())
                break

    except Exception as e:
        error = "发生错误%s" % e
        # raise indexError(error)
        field_error(error)


if __name__ == '__main__':
    print("""
        请提供三个必要参数，一个可选参数
        @work_path：程序工作路径
        @save_path：程序的保存路径
        @md5_path：[可选参数]指定一个由ThreadCopy生成的md5文件，将上一次备份的数据进行md5计算，并在第二次备份时跳过这些被标记过的数据，从而提高效率，节硬盘空间，留空或指定的文件无效则默认为不输入。
        @file_type：指定一个或多个筛选文件类型，请用[]包裹
        @move_default：[可选参数]是否移动，默认为否
        exp：work_path, save_path, md5_path, [file_type1, file_type_2], move_default"
        注意：Bate版本，请只用于测试。
        """)

    """
    work_path = "/Users/jeffrey/PycharmProjects"
    save_path = "/Users/jeffrey/test"
    md5_path = ""
    file_type = "[png,jpg,pdf,md]"
    move_default = False
    """

    work_path = input("请指定工作路径，必须参数：")
    save_path = input("请指定保存路径，必须参数：")
    md5_path = input("请指定md5文件路径，留空则默认不指定：")
    file_type = input("请指定文件类型，必须参数：")
    move_default = input("请指定是否移动，留空则默认为False")

    if move_default != "True":
        move_default = False

    if md5_path == "":
        md5_path = "null"

    if " " in work_path or " " in save_path or " " in md5_path:
        if not work_path.startswith('"') or not work_path.endswith('"') or not work_path.startswith(
                "'") or not work_path.endswith("'"):
            work_path = work_path.replace('"', "").replace("'", "")
            work_path = '"' + work_path + '"'

        if " " in save_path:
            if not save_path.startswith('"') or not save_path.endswith('"') or not save_path.startswith(
                    "'") or not save_path.endswith("'"):
                save_path = save_path.replace('"', "").replace("'", "")
                save_path = '"' + save_path + '"'

        if not md5_path == "null":
            if not md5_path.startswith('"') or not md5_path.endswith('"') or not md5_path.startswith(
                    "'") or not md5_path.endswith("'"):
                md5_path = md5_path.replace('"', "").replace("'", "")
                md5_path = '"' + md5_path + '"'

    if not os.path.exists(work_path):
        field_error("参数异常，原因是：指定的工作路径无效。")

    if not os.path.exists(save_path):
        field_error("参数异常，原因是：指定的保存路径无效。")

    # def run(work_path, save_path, md5_path, file_type, backups_default, begin):

    if not os.path.exists(md5_path):
        backups_default = False
    else:
        backups_default = True

    if not file_type.startswith("[") or file_type.endswith("]"):
        file_type.replace("[", "")
        file_type.replace("]", "")
        file_type = "[" + file_type + "]"

    typeListRe = re.compile(r"\[(.*?)\]").findall(file_type)
    typeList = list(str(typeListRe).replace("'", "").replace("[", "").replace("]", "").split(","))

    run(work_path, save_path, md5_path, typeList, backups_default, time.time())
