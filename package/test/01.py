#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 下午9:21
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : 01.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0

import threading
import time


def run(arg):
    print("running sub thread...{}".format(threading.current_thread()))
    threading.current_thread().name = "xurui_python"
    print("sub1 Thread...{}".format(threading.current_thread().getName()))
    print("sub2 Thread...{}".format(threading.current_thread().name))
    time.sleep(3)


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("t1",))
    t1.start()
    print("mian1 Thread...{}".format(threading.current_thread().getName()))
    print("mian2 Thread...{}".format(threading.current_thread().name))
