import os


def run():
    s, e = 0, 0
    errorList, dict_ = [], {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.split(".")[-1] == "jpg":
                try:
                    os.rename(file_path, file_path.replace(file_path.split(".")[-1], "jpeg"))
                    s += 1
                    print("已处理：" + file_path)
                except Exception as e:
                    errorList.append(e)
                    e += 1
                    dict_.setdefault(file_path, e)
    print("成功更改了{}个文件，发生了{}个异常\n".format(s, len(str(e))))

    for e in dict_:
        print("异常：" + e + ':' + dict_[e])


if __name__ == '__main__':
    path = r"/Users/jeffrey/test"
    run()
