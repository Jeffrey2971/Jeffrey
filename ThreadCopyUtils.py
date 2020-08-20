# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 上午2:39
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : ThreadCopyBeta.py
# @Software: MacOS 10.15.5

"""2020-7-1已归档"""
"""
ThreadCopyUtils功能介绍：
    1、可对指定目录实现多文件类型筛选复制或移动，并根据当前时间类型创建归档
    2、可对找到的文件生成md5文件，在下次指定这个文件时，被标记的文件不会被操作
本地测试（macOS）
    -------------------------------------------
    work_path = r"/Users/jeffrey/Desktop/new"       工作路径，大小：74G
    save_path = r"/Users/jeffrey/Desktop/split"     保存路径
    md5_path = r""                                  md5文件路径，大小：512KB 
    file_type = "[jpg,JPEG,mp4,MP4]"     文件类型，
    move_default = True                             移动
    测试结果
        总耗时：9
        发生异常：0
    -------------------------------------------
脚本地址：
    1、https://github.com/jeffrey2971/Jeffrey

- 转载请标明出处
"""

import datetime
import hashlib
import os
import queue
import re
import threading
import shutil
import time
import uuid
import math

"""global finish1 --> 解决采集线程的速度跟不上复制线程而break"""
thread_1 = False
thread_2 = False
tips = False
out = False


class indexError(Exception):
    print("""
        请提供三个必要参数和两个可选参数
            @work_path：【必要参数】程序工作路径
            @save_path：【必要参数】程序的保存路径
            @md5_path：[可选参数]指定一个由ThreadCopy生成的md5文件，将上一次备份的数据进行md5计算，并在第二次备份时跳过这些被标记过的数据，留空或指定的文件无效则默认为不输入。
            @file_type：【必要参数】指定一个或多个筛选文件类型，需要用[]包裹
            @move_default：[可选参数]是否移动，默认为否
        """)

    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        global out
        out = True
        return self.error_info


class index(object):

    def __init__(self, data):
        self.data = data
        self.moveDefault = move_default
        self.dataList = []
        self.typeList = []
        self.element = 0
        begin = time.time()

        """处理输入类型文件"""
        typeListRe = re.compile(r"\[(.*?)\]").findall(self.data)
        typeList = list(str(typeListRe).replace("'", "").replace("[", "").replace("]", "").split(","))
        for i in typeList:
            # """统一将列表中的元素转为小写"""
            # i = i.lower()
            self.typeList.append(i)

        """处理其他输入元素"""
        dataListTmp = self.data.split(",")

        """整理参数"""
        try:
            self.dataList.append(dataListTmp[0])
            self.dataList.append(dataListTmp[1])
            self.dataList.append(dataListTmp[2])
            self.dataList.append(typeList)

            """如果对应的MD5文件不合法则为false"""
            if os.path.exists(md5_path):
                """用户提供了正确的md5文件路径"""
                self.dataList.append(True)
            else:
                self.dataList.append(False)

            if self.dataList[0] == "":
                error = "必须提供一个工作路径"
                raise indexError(error)
            elif not os.path.exists(self.dataList[0]):
                error = ("%s不是一个有效的工作路径" % self.dataList[0])
                raise indexError(error)

            if self.dataList[1] == "":
                error = "必须提供一个保存路径"
                raise indexError(error)
            elif not os.path.exists(self.dataList[1]):
                error = "%s不是一个有效的保存路径" % self.dataList[1]
                raise indexError(error)

            if self.dataList[2] == 0:
                error = "必须至少提供一个类型参数"
                raise indexError(error)

            if self.dataList[0] in self.dataList[1]:
                error = "保存目录不能在工作目录内，否则将发生数据异常"
                raise indexError(error)

            """
            self.dataList[0]：工作路径                   --> str
            self.dataList[1]：保存路径                   --> str
            self.dataList[2]：md5文件路径                --> str
            self.dataList[3]：文件类型                   --> list
            self.dataList[4]：md5文件路径是否有效          --> boolean
            begin：脚本启动时间                            --> time.time
            """
            main(self.dataList[0], self.dataList[1], self.dataList[2], self.dataList[3], self.dataList[4], begin)

        except Exception as e:
            error = "参数异常：%s" % e
            raise indexError(error)


"""简单调试方法，出现未知错误时可传入信息调用该方法"""


def debug(data):
    make_file_ifNotExists = save_path + os.sep + "debug"
    if not os.path.exists(make_file_ifNotExists):
        os.mkdir(make_file_ifNotExists)
    with open(make_file_ifNotExists + os.sep + "debug.log", mode="a") as d:
        d.write("##########################################" + "\n")
        d.write("时间：" + str(datetime.datetime.now()) + "\n")
        d.write("信息：" + "\n")
        d.write(data)
        d.write("\n" + "##########################################")


def write_md5(file, path, thread_error):
    global md5
    try:
        with open(file, mode="rb") as f:
            md5 = str(hashlib.md5(f.read()).hexdigest())
            with open(path + os.sep + "md5.log", mode="a") as m:
                global tips
                if not tips:
                    m.write("\r\n")
                    tips = True
                m.write(md5 + "\n")
    except IOError as e:
        thread_error.append(e)
        print("计算或写入md5时出错：" + str(e))
    finally:
        return 0


"""Thread1负责采集资源"""


class Thread1(threading.Thread):
    def __init__(self, work_path, file_type, save_path, data_queue, wait_queue, backups_default, old_list,
                 thread_error):
        threading.Thread.__init__(self)
        self.workPath = work_path
        self.savePath = save_path
        self.fileType = file_type
        self.dataQueue = data_queue
        self.waitQueue = wait_queue
        self.default = backups_default
        self.checkList = []
        self.fileTypeTmp = []
        self.oldMd5List = old_list
        self.threadError = thread_error

    def run(self):
        global findNum
        findNum = 0
        global lostNum
        lostNum = 0
        for x in self.fileType:
            self.fileTypeTmp.append(x)
        while True:
            try:
                if len(self.fileTypeTmp) != 0:
                    for w in self.fileTypeTmp.copy():
                        for home, dirs, files in os.walk(self.workPath):
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
                                                findNum += 1
                                            else:
                                                self.waitQueue.put(path)
                                        else:
                                            """跳过"""
                                            pass
                                    else:
                                        if path.split(os.sep)[-1] not in self.checkList:
                                            self.dataQueue.put(path)
                                            self.checkList.append(path.split(os.sep)[-1])  # 文件名.后缀名
                                            findNum += 1
                                        else:
                                            self.waitQueue.put(path)
                                else:
                                    lostNum += 1
                        self.fileTypeTmp.remove(w)
                print("\n")
                print("采集线程完成，共找到{}个文件，过滤了{}个文件".format(str(findNum), str(lostNum)))

                global thread_1
                thread_1 = True  # 需声明采集已经结束
                break  # 找的速度跟不上取的速度会发生异常
            except Exception as e:
                self.threadError.append(e)
                error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                print("\n")
                print(error)


"""Thread2负责复制或移动文件"""


class Thread2(threading.Thread):

    def __init__(self, data_queue, save_path, file_type, begin, wait_queue, thread_error):
        threading.Thread.__init__(self)
        self.dataQueue = data_queue
        self.savePath = save_path
        self.fileType = file_type
        self.beginTime = begin
        self.waitQueue = wait_queue
        self.threadError = thread_error

    def run(self):
        global file
        global cmNum
        cmNum = 0
        global renameNum
        renameNum = 0
        global size_all
        size_all = 0

        while True:
            try:
                if self.dataQueue.empty() and thread_1:
                    """处理重名文件"""
                    if self.waitQueue.maxsize != 0:
                        """重名文件队列"""
                        path = self.waitQueue.get()
                        """计算文件的md5值并写入到文件中"""
                        write_md5(path, self.savePath, self.threadError)
                        """End"""
                        renameNum += 1
                        try:
                            if move_default is True:
                                shutil.move(path,
                                            self.savePath + os.sep + path.split(os.sep)[-1] + "." + str(
                                                uuid.uuid4()) + "." +
                                            path.split(".")[-1])
                                cmNum += 1

                            else:
                                shutil.copyfile(path,
                                                self.savePath + os.sep + path.split(os.sep)[-1] + "." + str(
                                                    uuid.uuid4()) + "." +
                                                path.split(".")[-1])
                                cmNum += 1
                        except Exception as e:
                            error = """
                            异常报告：
                            所在线程：%s
                            异常文件：%s
                            发现异常：%s
                            """ % (threading.current_thread().getName(), path, e)
                            self.threadError.append(error)
                            error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                            print("\n")
                            print(error)
                    for L in self.fileType:
                        for w in os.listdir(self.savePath):
                            if w.endswith(L):
                                shutil.move(self.savePath + os.sep + w, self.savePath + os.sep + L)
                                print("\n")
                                print("正在归档：{}".format(self.savePath + os.sep + w))
                    global thread_2
                    thread_2 = True
                    break

                elif not self.dataQueue.empty():  # 假如不为空
                    try:
                        """如果dataQueue没有值，执行取值操作会卡死且不报错"""
                        """不重名的文件队列"""
                        file = self.dataQueue.get()
                        """计算文件的md5值并写入到文件中"""
                        write_md5(file, self.savePath, self.threadError)

                        """End"""
                        size_all += os.path.getsize(file)
                        if move_default is True:
                            shutil.move(file, self.savePath)
                            cmNum += 1

                        else:
                            shutil.copy(file, self.savePath)
                            cmNum += 1


                    except Exception as e:
                        error = """
                            异常报告：
                            所在线程：%s
                            异常文件：%s
                            发现异常：%s
                            """ % (threading.current_thread().getName(), file, e)
                        self.threadError.append(error)
                        error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                        print("\n", error, "\n")
            except Exception as e:
                self.threadError.append(e)
                error = "所在线程：%s发生错误：%s" % (threading.current_thread().getName(), e)
                print("\n")
                print(error)


def main(work_path, save_path, md5_path, file_type, backups_default, begin):
    global result
    try:
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
        dataQueue = queue.Queue()
        waitQueue = queue.Queue()
        threadError = []

        """创建并启动线程传递相关参数"""
        T1 = Thread1(work_path, file_type, save_path, dataQueue, waitQueue, backups_default, oldMd5List, threadError)
        T2 = Thread2(dataQueue, save_path, file_type, begin, waitQueue, threadError)
        T1.start()
        T2.start()

        if move_default:
            mode = "移动"
        else:
            mode = "复制"

        """逻辑堵塞主线程"""
        while True:
            if out:
                print("程序异常将终止！")
                print("\a")
                exit()

            if dataQueue.empty() and waitQueue.empty() and thread_1 and thread_2:
                T1.join()
                T2.join()
                try:
                    endTime = time.time()
                    """处理类型文件"""
                    sizeGB = "%.2f" % (size_all / 1024 / 1024 / 1024)
                    sizeMB = "%.2f" % (size_all / 1024 / 1024)
                    total = "%.2f" % (endTime - begin)
                    minute = float(total) / 60
                    if minute < 1:
                        minute = 0
                    print("\n")
                    result = ("已完成，共" + mode + "了" + str(cmNum) + "个文件，处理了" + str(renameNum) + "个重名文件，发生了" + str(
                        len(threadError)) + "个异常，忽略了" + str(
                        lostNum) + "个文件，总大小为" + sizeGB + "GB，" + sizeMB + "MB，" + "耗时" + str(
                        math.floor(minute)) + "分" + str(total) + "秒")
                    print(result)
                    print("\n")
                    print("结束线程：", threading.current_thread())
                    with open(save_path + os.sep + "md5.log", mode='r+') as tips:
                        content = tips.read()
                        tips.seek(0, 0)
                        tips.write(
                            "这个备份文件创建于：" + str(datetime.datetime.now()) + "，为了确保下次备份的正确性，请不要修改以下的内容" + "\n\n" + content)
                finally:
                    try:
                        """创建日志报告信息"""
                        with open(save_path + os.sep + "report.log", mode="a") as f:
                            for e in threadError:
                                f.write("------错误报告------" + '\n' + str(e) + '\n')
                            f.write("------其他信息------" + '\n' + result + '\n')
                        print("已生成日志：" + save_path + os.sep + "report.log")
                        if os.path.exists(save_path + os.sep + "md5.txt"):
                            print("生成md5文件失败")
                        else:
                            print("已生成md5文件：" + save_path + os.sep + "md5.txt")
                    except Exception as e:
                        print("生成日志失败：", e)
                    finally:
                        print("程序退出", threading.current_thread())
                        print("\a")
                        break
            """显示线程反馈信息"""
            print(
                "\r提示：当前已找到：{}个文件，已忽略了{}个文件，已{}了{}个文件，剩余{}个文件，已发现了{}个重名文件，已处理了{}个重名文件，发生了{}个线程异常\t".format(
                    str(findNum),
                    str(lostNum),
                    mode,
                    str(cmNum),
                    int(findNum - cmNum),
                    str(waitQueue.maxsize),
                    str(renameNum),
                    str(len(threadError))),
                end="")

    except Exception as e:
        error = "发生错误%s" % e
        raise indexError(error)
    finally:
        exit()


if __name__ == '__main__':
    """
        请提供三个必要参数，三个可选参数
        @work_path：程序工作路径
        @save_path：程序的保存路径
        @md5_path：[可选参数]指定一个由ThreadCopy生成的md5文件，将上一次备份的数据进行md5计算，并在第二次备份时跳过这些被标记过的数据，从而提高效率，节硬盘空间，留空或指定的文件无效则默认为不输入。
        @file_type：指定一个或多个筛选文件类型，需要用[]包裹，需注意，程序区分后缀名大小写，如发现部分文件没有被复制或移动，可能是文件类型问题，例如 jpg 和 jpeg
        @move_default：[可选参数]是否移动，默认为否
    """

    try:
        print("\n\n")
        """Data"""
        work_path = r"/Users/jeffrey/IdeaProjects"
        save_path = r"/Users/jeffrey/test"
        md5_path = r""
        file_type = "[md,Md,MD.mD]"
        move_default = False
        """"""

        if md5_path == "":
            md5_path += "null"
        # file_type = ([w.lower() for w in file_type])
        data = work_path + ", " + save_path + ", " + md5_path + ", " + file_type
        index(data.replace(" ", ""))
    except Exception as e:
        error = "发生错误%s" % e
        raise indexError(error)