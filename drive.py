# !/usr/bin/env python
import os
import sys

"""
此脚本用于在Ubuntu系统下挂载iPhone
请正常使用，不确定其稳定性
"""

# 这是你的设备挂载点，可自定义
path = "/Users/jeffrey/test"


def check_path():
    if os.system("dpkg --list | grep libimobiledevice-utils") == 0:  # 所需包
        if os.system("dpkg --list | grep ifuse") == 0:  # 所需包
            if os.path.exists(path) is False:
                if os.system("mkdir " + path) == 256:  # 防止为卸载情况下拔出设备
                    if os.system("fusermount -u " + path) == 0:
                        os.system("notify-send " + "检测到上次未正常拔出，已修复")
                check_path()

            else:
                if os.system("idevicepair pair") == 256 or os.system("idevicepair pair") == 0:  # Bug语句
                    os.system("usbmuxd - f - v")
                    if os.system("ifuse " + path) == 0:  # 挂载
                        os.system("notify-send " + "挂载成功，但请注意需弹出设备时需次运行此脚本后再退出！")
                        os.system("nautilus " + path)  # 打开目录
                    else:
                        os.system("fusermount -u " + path)  # 卸载
                        os.system("rmdir " + path)  # 移除载入点
                        os.system("notify-send " + "已卸载，可拔出设备！")
                else:
                    os.system("notify-send " + "请插入设备！")
                    quit()
        else:
            print('请执行：sudo apt install ifuse')
            os.system("notify-send " + "缺少包：ifuse")

    else:
        print('请执行：sudo apt install libimobiledevice6 libimobiledevice-utils')
        os.system("notify-send " + "缺少包：libimobiledevice6 libimobiledevice-utils")


if __name__ == '__main__':
    if sys.platform == "linux":
        if path == "":
            print("请先定义挂载点")
            exit()
        check_path()
    else:
        print("该脚本只能在Linux下运行！")
