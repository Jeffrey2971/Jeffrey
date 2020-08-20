import hashlib
import os

"""
根据计算 md5 删除指定路径中相同的文件
"""

path = r"/Users/jeffrey/PycharmProjects"


def run():
    global find_num
    global del_num
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            find_num += 1
            try:
                with open(file_path, mode="rb") as f:
                    md5 = str(hashlib.md5(f.read()).hexdigest().replace("\n", ""))
                    if md5 not in md5List:
                        md5List.append(md5)
                        print("放行：" + file_path)
                    else:
                        sameList.append(file_path)
                        delList.append(file_path)
            except:
                pass

    for i in delList:
        try:
            os.remove(i)
            global del_num
            del_num += 1
            print("已删除：" + i)
        except Exception as e:
            dict_del_error.setdefault(i, e)

    print(
        "\n共查找了：" + str(find_num) + " 个文件，发现了 " + str(len(sameList)) + " 个相同文件，成功删除了 " + str(del_num) + " 个文件，发生了 " + str(
            len(dict_del_error)) + " 个异常\n")
    for d in dict_del_error:
        print("删除 " + d + "失败，原因是：" + dict_del_error[d])


if __name__ == '__main__':
    md5List = []
    delList = []
    sameList = []
    dict_del_error = {}
    find_num = 0
    del_num = 0
    run()
