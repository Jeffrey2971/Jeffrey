#  需求：获取指定文件内有多少行内容

path = 'C:\\Users\\Administrator.USER-20191115PO\\Desktop\\test.txt'


def read_file():
    global a
    f = open(path)
    count = len(f.readlines())
    f = open(path)
    a = {}
    for line, i in zip(f, range(count)):
        a[i] = line.strip('\n')
    return

read_file()
print(a)