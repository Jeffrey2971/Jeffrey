# 大小写转换

phrase = 'Jeffrey Home'
print(phrase.lower())  # .lower()方法可将字符串转换为小写

print(phrase.upper())  # .upper()方法可将字符串转换为大写

# 判断字符串内是否都是大写或小写，用布尔类型返回True和False返回结果

print(phrase.islower())  # 用islower()方法判断字符串内是否都为小写，结果为False

print(phrase.isupper())  # 用isupper()方法判断字符串内是否都为大写，结果为False

print(phrase.lower().islower())  # 使用.lower()方法后再用.islower()方法判断字符是否都为小写，结果是True

print(phrase.upper().isupper())  # 使用.upper()方法后再用.isupper()方法判断字符是否都为大写，结果是True

print(len(phrase))  # len()方法可以获取字符串的长度

phrase = 'Jeffrey'
         #0123456...->字符排序默认从左到右从0开始

print(phrase[0])  # 如需取得字符串内指定位数字的话可在[]内输入字符串的数位，如超出最大范围数位则会报错

print(phrase.index('r'))  # .index 方法可以取得字符的数位，如字符不在字符串内则会报错

phrase = 'My name is Jeffrey'

print(phrase.replace('Jeffrey', 'Mable'))  # 使用 .replace()方法可以更改字符串内的内容

user_name = input('Enter your name：')  # 使用input()函数可让用户输入
user_age = input('Enter your age：')
print('Hello ' + user_name + '！' + 'Your are ' + user_age + ' years old!')

