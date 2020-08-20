#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 下午9:24
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : NoThreadTest.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

"""
测试非多线程耗时：
    工作路劲：/home/jeffrey
    保存路径：/home/jeffrey/test
    复制文件数量：5407
    总耗时：14.274111986160278
"""

import os
import shutil
import time

beginTime = time.time()

workPath = r"/home/jeffrey/PycharmProjects"
savePath = r"/home/jeffrey/test"
fileType = "md"
move = False


def hello():
    print("====================================\n")
    workPath = input("请输入一个工作路径：")
    savePath = input("请输入文件保存路径：")
    fileType = bool(input("请输入"))


def get_file_list():
    """
    此模块作用于对指定目录进行遍历，
    筛选出匹配的文件类型并放入fileList列表中
    :return: fileList
    """
    fileList = []
    lostNum = 0
    findNum = 0
    for home, dirs, files in os.walk(workPath):
        for filename in files:
            path = os.path.join(home, filename)
            if path.endswith(fileType):
                fileList.append(path)
                findNum += 1
                print("已找到" + str(findNum) + "个文件")
            else:
                lostNum += 1
                print("已过滤" + str(lostNum) + "个文件")
    return fileList


def copy_or_move(after_file_list):
    """
    此模块对作用于对筛选出的文件根据是复制或移动到指定文件夹
    :return: finish
    """
    num = 0
    for file in after_file_list:
        if move is True:
            shutil.move(file, savePath)
            num += 1
            print("已移动" + str(num) + "个文件：" + file)
        else:
            shutil.copy(file, savePath)
            num += 1
            print("已复制" + str(num) + "个文件：" + file)
    endTime = time.time()
    print("总耗时：", endTime - beginTime)
    print("\n已完成")
    quit()


if __name__ == "__main__":
    if workPath == "":
        print("请提供工作路径")
    elif not os.path.exists(workPath):
        print("指定工作路劲无效")

    if savePath == "":
        print("请提文件保存路径")
    elif not os.path.exists(savePath):
        print("指定文件保存路径无效")

    if fileType == "":
        print("请提供指定文件类型")

    fileList = get_file_list()
    copy_or_move(fileList)
