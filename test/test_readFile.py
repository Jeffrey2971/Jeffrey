import os
import shutil

workPath = r"/Users/jeffrey/IdeaProjects"
savePath = r"/Users/jeffrey/test"

for home, dirs, files in os.walk(workPath):
    for filename in files:
        path = os.path.join(home, filename)
        if "约束" in path.split(os.sep)[-1]:
            shutil.copy(path, savePath)
            print(path)
print("结束")
