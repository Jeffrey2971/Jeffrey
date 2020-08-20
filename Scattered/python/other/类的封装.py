class Card(object):
    def __init__(self, id, pwd, balance):
        self.id = id  # 卡号
        self.pwd = pwd  # 密码
        self.__balance = balance  # 余额,如在balance前加上双下划线__则表示为私有属性并只能在类的内部进行访问

    def deposit(self):
        print('存款')

    def getBalance(self, idd, pwdd):
        if idd == self.id and pwdd == self.pwd:
            return '输入正确，您的余额为：' + str(self.__balance)
        else:
            return '密码错误'


card = Card('10086', '123456', 100000000000)


# 如在类的方法内使用了双下划线则在外部无法直接访问到内部变量
# print(card.balance) 错误
# print(card.__balance) 错误

enter_id = (input('请输入卡号：'))
enter_pwd = (input('请输入密码：'))


print(card._Card__balance)

print(card.getBalance(enter_id, enter_pwd))











