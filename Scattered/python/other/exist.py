x = int(input('请输入第一个数字：'))
y = int(input('请输入第二个数字：'))

def test(x,y):
    if x > y:
        return x
    elif x < y:
        return x+y

test(x,y)