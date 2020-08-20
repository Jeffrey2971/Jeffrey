
#表达式：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
#1，1，2，3，5，8，13，21，34，55。。。。。


def test(num):
    if num==1 or num==2:
        return 1
    return test(num-1)+test(num-2)

test(5)