class Animal(object):
    def __init__(self, color):
        self.color = color

    def eat(self):
        print('动物再吃！')

    def run(self):
        print('动物在跑！')

class Cat(Animal):  # Cat 继承animal类
    def eat(self):
        print('猫在吃鱼')


class Dog(Animal):
    def __init__(self, name, age, color):
        super(Dog, self).__init__(color)  # 调用父类初始化方法
        self.name = name
        self.age = age

    def eat(self):
         print('狗在啃骨头')


dog = Dog('小黑',10,'黑色')
print(dog.color)

# 多态
def feed(obj):
    obj.eat()

an = Animal('黄')
cat = Cat('橘色')
dog = Dog('小黑', 2, '黑色')
feed(an)