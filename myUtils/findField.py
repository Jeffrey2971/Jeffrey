import os
import shutil

"""查找带有关键字的文件"""

work_path = r"/Users/jeffrey/IdeaProjects"
field = ["chm", "CHM", "Chm"]
found = []
copy = True

num = 0
for root, dirs, files in os.walk(work_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.splitext(file_path)[-1].replace(".", "") in field:
            print(file_path)
            found.append(file_path)
            num += 1
if copy:
    for i in found:
        shutil.copy(i, "/Users/jeffrey/test/found/")

print("已完成，共找到了：" + str(num) + "个文件")
with open("/Users/jeffrey/test/found.txt", mode="a") as f:
    for i in found:
        f.write(i + "\n")



