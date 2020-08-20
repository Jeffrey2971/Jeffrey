# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 19:08
# @Software: PyCharm
# @File    : movieMove.py
# @Version : 3.7
# @Author  : Jeffrey

"""
处理电视剧给老妈看
"""

import os
import time
import shutil

downed_list = ['03.mp4', '42.mp4', '45.mp4', '53.mp4', '54.mp4', '55.mp4', '56.mp4', '57.mp4', '63.mp4', '65.mp4', '66.mp4', '67.mp4', '68.mp4', '12.mp4', '32.mp4', '34.mp4', '36.mp4', '37.mp4', '41.mp4', '44.mp4', '47.mp4', '50.mp4', '51.mp4', '08.mp4'] #存放以及拷贝的文件名
path = r'e:\yxgl3\02555 延禧攻略 (2018)国二三.[看好剧关注微信公众号鲤鱼剧集频道 ：lyjjpd]'
s = r'g:\yxgl1'
num = 0
while True:
    files = os.listdir(path)
    for i in files:  # .xxx
        if i not in downed_list:
            if os.path.splitext(i)[1] == '.mp4':  # 假如文件名的扩展名为mp4
                r_path = path + '\\' + i
                g_size = os.path.getsize(r_path)
                f_size = g_size/float(1024 * 1024)
                print('[发现一个新的视频]：', i, '[文件大小]：', f_size, '[正在保存到]：', s)
                shutil.copy(r_path, r'g:\yxgl1')
                downed_list.append(i)
                for x in downed_list:
                    print('[保存完毕，等待一分钟后继续检测，已保存的文件有]：', x)
                time.sleep(60)
                if len(downed_list) == '70':
                    print('下载完毕')
                    break
        num += 1
        print('当前没有视频，等待新的文件下载完毕', num)
        time.sleep(2)
