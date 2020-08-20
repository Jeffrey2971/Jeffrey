import hashlib
import os

"""计算目录下的md5"""
path = r"/Users/jeffrey/Desktop/bak"

for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        print("正在计算：" + file_path)

        with open(file_path, mode="rb") as f:
            md5 = str(hashlib.md5(f.read()).hexdigest().replace("\n", ""))
            with open(path + os.sep + "md5.log", mode="a") as m:
                m.write(md5 + "\n")
