#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 下午2:34
# @Author  : @Jeffrey
# @Email   : Jeffrey2971@outlook.com
# @File    : 快捷路径.py
# @Software: Ubuntu 18.04.4 LTS python3.8.0
import os

password = "Aa664490254"


def sys():
    print("""
    1：/usr/local
    2：/usr/share
    3：/opt
    4：/etc
    5：/usr/share/applications

    """)
    data = input("请输入指定编号：")
    if data == "1":
        os.system("echo " + password + "|sudo -S nautilus /usr/local")
    elif data == "2":
        os.system("echo " + password + "|sudo -S nautilus /usr/share")
    elif data == "3":
        os.system("echo " + password + "|sudo -S nautilus /opt")
    elif data == "4":
        os.system("echo " + password + "|sudo -S nautilus /etc")
    elif data == "5":
        os.system("echo " + password + "|sudo -S nautilus /usr/share/applications")


def tomcat():
    print("""
    1：/etc/tomcat8
    2：/usr/share/tomcat8
    3：/var/log/tomcat8
    4：/var/lib/tomcat8
    
    """)
    data = input("请输入指定编号：")
    if data == "1":
        os.system("echo " + password + "|sudo -S nautilus /etc/tomcat8")
    elif data == "2":
        os.system("echo " + password + "|sudo -S nautilus /usr/share/tomcat8")
    elif data == "3":
        os.system("echo " + password + "|sudo -S nautilus /var/log/tomcat8")
    elif data == "4":
        os.system("echo " + password + "|sudo -S nautilus /var/lib/tomcat8")


def pycharm():
    pass


def idea():
    pass
exit()

def index():
    print("""
    1：sys
    2：tomcat
    3：pycharm
    4：idea
    """)
    data = input("请输入指定编号：")
    if data == "1":
        sys()
    elif data == "2":
        tomcat()
    elif data == "3":
        pycharm()
    elif data == "4":
        idea()


if __name__ == '__main__':
    index()
    tomcat()
    pass
