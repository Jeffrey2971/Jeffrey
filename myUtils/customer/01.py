import os
import threading
import queue
import shutil

"""
现在是直接运行吗？
"""
work_path = os.getcwd()
"""
你看看我这个朋友写的，我运行一下给你看不行的话用你的
"""
save_path = os.getcwd() + os.sep + "22"
if not os.path.exists(save_path):
    try:
        os.mkdir(save_path)
    except Exception as e:
        pass


def debug(data):
    try:
        debug_path = save_path + os.sep + "debug.log"
        if not debug_path:
            os.mkdir(debug_path)
        with open(save_path + os.sep + "debug.log", mode="a") as d:
            d.write(data)
    except Exception as debugLog:
        print(debugLog)


def run():
    passNum = 0
    copyNum = 0
    for home, dirs, files in os.walk(work_path):
        for filename in files:
            path = os.path.join(home, filename)
            if path.split(os.sep)[-1] == "index.html":
                debug(path)
                if path != "index.html":
                    continue
                else:
                    path_dir = home.split(os.sep)[-1]
                    try:

                        print(path, save_path + os.sep + path_dir + ".html")

                        shutil.move(path, save_path + os.sep + path_dir + ".html")
                        copyNum += 1
                        print("已移动" + str(copyNum) + "个文件")
                    except Exception as e:
                        print("移动" + path + "失败，原因是：" + str(e))
                        exit()
            passNum += 1
            print("已忽略" + str(passNum) + "个文件")


if __name__ == '__main__':
    run()
    os.system("echo 已完成！")
    os.system("pause>nul")
