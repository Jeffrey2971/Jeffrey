import hashlib
import os
import shutil

"""
根据md5文件标记，复制新文件夹中的文件到旧文件夹中
"""
new_file_md5 = []
new_file_path = []


def template(data, file_md5_list):
    data_list = []
    num = 0
    lost = 0
    check = 0
    copy = 0

    for root, dirs, files in os.walk(data):
        for file in files:
            file_path = os.path.join(root, file)
            if finish:
                mode = "检查"
            else:
                mode = "读取"
            print(
                "\r提示：当前已{}{}个文件，已找到{}个文件，已复制{}个文件，已忽略{}个文件，进度{}/3\t".format(str(mode), str(check), str(num), str(copy),
                                                                      str(lost), str(progress)), end="")
            with open(file_path, mode="rb") as f:
                md5 = str(hashlib.md5(f.read()).hexdigest().replace("\n", ""))
                if finish:
                    if md5 in file_md5_list:
                        num += 1
                        shutil.copy(file_path, different_path)
                        copy += 1
                    else:
                        lost += 1
                data_list.append(md5)
                check += 1
    return data_list


def main():
    """"""
    global progress
    progress = 0
    progress += 1
    old = template(resource_path, None)
    progress += 1
    new = template(target_path, None)

    md5_list = list((set(old) ^ set(new)))
    global finish
    finish = True
    if len(md5_list) >= 1:
        progress += 1
        template(target_path, md5_list)
        print("已完成")
    else:
        print("没有找到的文件。")


if __name__ == '__main__':
    finish = False

    resource_path = r"/Users/jeffrey/Desktop/obj/old"

    target_path = r"/Users/jeffrey/Desktop/obj/new"

    """如果target_path目录没有resource_path目录内的文件，那么这个文件将会被复制到different_path"""
    different_path = r"/Users/jeffrey/Desktop/obj/diff"

    main()
