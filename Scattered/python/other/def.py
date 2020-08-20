

def data(name,age,sex='girl',country='Malaysia'):#前两个为必须参数，后两个为默认参数
    print('我叫：'+str(name))
    print('我今年：'+str(age)+'岁')
    print('性别：'+str(sex))
    print('国籍：'+str(country))

data('mable',18)#调用函数
data('mable',18,sex='boy',country='China')#修改默认参数，可以不用按照顺序
data('mable',18,country='China',sex='boy')#修改默认参数，可以不用按照顺序