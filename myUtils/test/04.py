import os

path = r"/Users/jeffrey/test"  # 工作路径
file_type = []
pass_keyword = ["吕本伟", "马飞飞", "吃电脑"]  # 关键字
target_keyword = "aaa"  # 被替换的关键字


def function_1():
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".txt"):
                file_type.append(file_path)


def function_2():
    for i in file_type:
        with open(i, mode="r+") as f:
            for p in pass_keyword:
                tmp = f.read().replace(p, target_keyword)
                f.write(tmp)


def main():
    function_1()
    function_2()


if __name__ == '__main__':
    main()
