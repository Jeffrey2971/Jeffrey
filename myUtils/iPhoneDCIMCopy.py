import hashlib
import os
import shutil

"""
- 功能概述
    - 可以将指定目录内的图片或者视频等文件复制到iPhone设备中，比起其他第三方软件，更高效
- 特点
    - 脚本执行后会先检查目标路径(DCIM目录下)内所有文件的md5值，由于这些md5值是唯一的，所以在导入照片时可避免重复的照片，从而节省手机磁盘空间
    - 当资源目录下的文件无法被访问时程序不会中断而是会保存无法复制的文件到日志文件中
    - 可选移动或复制，默认为False
- 保存逻辑分析
    - IPHONE设备下的所有照片及视频等文件都保存在DCIM目录下，并分为从「100APPLE」开始，每个文件夹内保存1000个文件，当一个文件夹内的文件
    超过1000个以后，将会新建一个「101APPLE」，以此类推
- 注意事项
    - DCIM默认连接电脑没有，需要将IPHONE作为驱动器挂载
- 总结
    - 这种方式没用，在手机显示不出来照片等信息，甚至会得不偿失。。。

"""

"""资源目录"""
resources_path = r"/Users/jeffrey/IdeaProjects"

"""苹果手机的DCIM目录"""
target_path = r"/Users/jeffrey/test/DCIM"

targetMd5List = []
folderNumsList = []
errorList = []
finish = False
folderListMaxNum = 0


def template(data, folderListMaxNum):
    recursion = 0
    for root, dirs, files in os.walk(data):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                print("正在操作文件：" + file_path)
                with open(file_path, mode="rb") as f:
                    md5 = str(hashlib.md5(f.read()).hexdigest().replace("\n", ""))
                    if finish:
                        target_folder = target_path + os.sep + str(folderListMaxNum) + "APPLE"
                        if md5 not in targetMd5List:
                            if recursion >= 1000 and os.path.exists(target_folder):
                                folderListMaxNum += 1
                                os.mkdir(target_path + os.sep + str(folderListMaxNum) + "APPLE")
                                recursion = 0

                            if move_default:
                                shutil.move(file_path, target_folder)
                            else:
                                shutil.copy(file_path, target_folder)
                            recursion += 1
                        else:
                            pass
                    else:
                        targetMd5List.append(md5)
            except IOError as e:
                errorList.append("处理：" + file_path + "时发生了一个异常，这个文件不会被复制或移动，原因是：" + str(e))


def main():
    template(target_path, None)
    global finish
    finish = True

    """获取xxxAPPLE最大的数字"""
    folder = os.listdir(target_path)
    for i in folder:
        if "APPLE" in i:
            folderNumsList.append(i.replace("APPLE", ""))
        """target目录下数字最大的命名文件夹"""

    if len(folderNumsList) == 0:
        folderNumsList.append(100)

    folderListMaxNum = int(max(folderNumsList))

    if not folderListMaxNum == 100:
        folderListMaxNum += 1

    if os.path.exists(target_path + os.sep + str(folderListMaxNum) + "APPLE"):
        folderListMaxNum += 1

    os.mkdir(target_path + os.sep + str(folderListMaxNum) + "APPLE")
    template(resources_path, folderListMaxNum)

    with open(os.path.split(os.path.realpath(__file__))[0] + os.sep + "error.log", mode="a") as ew:
        for e in errorList:
            ew.write(str(e + "\n"))
            print(e)
        print("完成")


if __name__ == '__main__':
    move_default = False
    main()
