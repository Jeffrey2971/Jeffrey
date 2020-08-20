import os

"""删除带有关键字的文件"""

work_path = r"/Users/jeffrey/Desktop"
field = r"的副本"

num = 0
for root, dirs, files in os.walk(work_path):
    for file in files:
        file_path = os.path.join(root, file)
        if field in file_path:
            os.remove(file_path)
            num += 1
            print("已删除" + file_path)

print("已完成，共删除了：" + str(num) + "个文件")



