#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 下午2:12
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : zip.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

import os
import shutil
import random
import zipfile

# ----------DATA----------
# 完成后是否删除源文件

delete = True
# 是否级联，打开将增加耗时
cascade = True
# 是否完整保存到指定目录，打开将增加耗时
SavePathAll = False
# 解压密码，默认为空
PassCode = ''
# 工作路径，必须提供
WorkPath = '/home/jeffrey/桌面/JavaWeb1'
# 不填默认解压到相对于目录下
SavePath = '/home/jeffrey/桌面/javaweb2'

# ----------END----------
WorkPathTmp = WorkPath


def find():
    """
    本模块用于获取指定目录下（包括子目录）的所有zip文件，并获取级联zip文件。
    dataList 用于存放源zip文件
    cascadeList 用于存放级联zip文件
    """
    data_list = []
    cascade_list = []
    for root, dirs, files in os.walk(WorkPath):
        for i in range(len(files)):
            if files[i][-3:] == "zip":
                file_path = root + '/' + files[i]  # zip所在完整位置
                data_list.append(file_path)
                if cascade is True:
                    extracting = zipfile.ZipFile(file_path)
                    for c in extracting.namelist():
                        if c.split(".")[-1] == "zip":
                            file_path = file_path.replace(".zip", "")
                            cascade_list.append(os.path.abspath(os.path.join(file_path, "./")) + "/" + c)
                    extracting.close()
    return data_list, cascade_list


path_default = True
err = []

def do():

    num = 0
    del_num = 0
    deleteList = []

    if path_default is True:
        d = find()
        """
        d[0]  普通数据
        d[1]  级联数据
        """
        for L in d[0]:
            extracting = zipfile.ZipFile(L)
            extracting.extractall(L.replace(".zip", ""))
            num += 1
            print("已处理：" + str(num) + "：" + L)
            extracting.close()
            if delete is True:
                deleteList.append(L)
        if cascade is True:
            for C in d[1]:
                extracting = zipfile.ZipFile(C)
                extracting.extractall(C.replace(".zip", ""))
                num += 1
                print("已处理级联数据：" + str(num) + "：" + C)
                extracting.close()
                if delete is True:
                    deleteList.append(C)
        if delete is True:
            for d in deleteList:
                os.remove(d)
                del_num += 1
                print("已删除：" + str(del_num) + "：" + d)
        print("操作完成，共处理了：" + str(num) + "个文件，删除了：" + str(del_num) + "个文件")
        return num, del_num
    else:
        tmp = "/tmp/zip_bak" + str(random.randint(1, 99))
        if os.path.exists(tmp) is True:
            shutil.rmtree(tmp)
        print("正在备份文件，请稍后")
        shutil.copytree(WorkPathTmp, tmp)
        global WorkPath
        WorkPath = tmp
        result_1 = find()
        for L in result_1[0]:
            extracting = zipfile.ZipFile(L)
            extracting.extractall(L.replace(".zip", ""))
            num += 1
            print("已处理：" + str(num) + "：" + L)
            extracting.close()
            if delete is True:
                deleteList.append(L)
        try:
            if cascade is True:
                for C in result_1[1]:
                    extracting = zipfile.ZipFile(C)
                    extracting.extractall(C.replace(".zip", ""))
                    num += 1
                    print("已处理级联数据：" + str(num) + "：" + C)
                    extracting.close()
                    if delete is True:
                        deleteList.append(C)
        except Exception as e:
            err.append(e)

        if delete is True:
            for d in deleteList:
                os.remove(d)
                del_num += 1
                print("已删除：" + str(del_num) + "：" + d)
        print("正在移动文件到：：" + SavePath)
        shutil.move(tmp, SavePath)
        for e in err:
            print("处理时发生的错误：" + e)
        print("操作完成，共处理了：" + str(num) + "个文件，删除了：" + str(del_num) + "个文件")
        return num, del_num


if __name__ == '__main__':
    def out():
        print("已终止！")
        exit()


    def work_path():
        if WorkPath == '':
            print("请输入工作路径")
        elif os.path.exists(WorkPath) is False:
            print("工作路径不存在")
        elif any(key in WorkPath.split("/")[-1] for key in ['/', '\\', ':', '|', '*', '<', '>', '?', '"']):
            print("指定文件夹有非法字符")
        else:
            return True
        return False


    def save_path():

        if SavePath == "":
            print("将默认保存到对应目录下")

            return True
        else:
            global path_default
            path_default = False
            if os.path.exists(SavePath) is False:
                print("定义的保存路径不存在")
            elif any(key in SavePath.split("/")[-1] for key in ['/', '\\', ':', '|', '*', '<', '>', '?', '"']):
                print("指定的保存路径文件夹含有非法字符")
            elif SavePath[-1] == "/" or SavePath == "\\":
                print("指定的保存路径文件夹尾部默认不得有正反斜杠")
            else:
                return True
            return False


    if work_path() is True:
        if save_path() is True:
            do()
    else:
        out()
