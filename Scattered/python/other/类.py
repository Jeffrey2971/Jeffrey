'''
class Men():
    gender = 'girl'  # 类变量(描述类的通俗特征，只与类有关)
    avg_height = 1.6  # 类变量(描述类的通俗特征，只与对象有关，这里的对象指实例化后的对象)

    def __init__(self, name, age):  # 初始化`对象特征
  # 使用构造函数的好处：
  # 1、初始化对象的特征
  # 2、保存了对象的特征
            self.name = name  # 实例变量(保存对象的具体特征)
            self.age = age  # 实例变量(保存对象的具体特征)
            pass  # 该处的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。

    def sleep(self):  
        print('sleeping')

    def think(self):
        print('thinking')


men = Men('mable', 18)  # 对象实例化

print(men.name, men.age)
print(men.__dict__)  # 查看具体对象并以字典形式返回

'''


class Dog(object):

    type = '宠物'  # 类变量

    def __init__(self, name, age, color):  # 初始化方法，self表示当前对象
        self.name = name  # 实例变量
        self.age = age
        self.color =color

    def eat(self):  # 普通方法
        print(self.name, '狗狗在啃骨头！')

    def run(self, speed):
        print(self.run, '狗狗在奔跑!速度：', speed, '每秒')
        #      dog.run


dog = Dog('小黄', 3, '黑色')  # 对象实例化，括号内填写__init__内定义除了self外变量，隐式传递了self
dog.color = '黄色'  # 修改类变量
print(dog.color)

dog.eat()
dog.run('3m')
