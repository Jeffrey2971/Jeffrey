'''
# 总结
# ^ 匹配字符串的开始。
# $ 匹配字符串的结尾。
# \b 匹配一个单词的边界。
# \d 匹配任意数字。
# \D 匹配任意非数字字符。
# x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
# x* 匹配0次或者多次 x 字符。
# x+ 匹配1次或者多次 x 字符。
# x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
# (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
# (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
# 正则表达式中的点号通常意味着 “匹配任意单字符”



正则字符                    释义                          举例

+                      前面元素至少出现一次           ab+:ab、abbbb等

*                   前面元素至少出现0次或多次       ab*:a、ab、abb 等

?                   匹配前面的一次或0次              Ab:A、Ab 等

^                   作为开始标记                     ^a:abc、aaaaaa等

$                   作为结束标记                      c$:abc、cccc 等

\d                  数字                              4、9 等

\D                  非数字                            a、-  等

[a-z]               a-z之间的任意字母              a、p、m 等

[0-9]               0-9之间的任意数字              0、2、9 等

'''


import re

# findall

#  re.findall(pattern,string,flage=0)

# pattern 指的是，正则表达式匹配规则
# string 指的是，要进行匹配的字符串
# flags 指的是，可选参数，进行指定条件的匹配


# 需求：匹配字符中所有的Jeffrey

test = 'lemon&apple&pear&lemoon&lemooon&lemoooon&lemoooooooooon'

result = re.findall('lemon', test)  # 普通字符

# 需求：除了匹配lemon，还需把其他的lemoon,lemooon,lemoooon给匹配出来

result_1 = re.findall('lemo{3,10}n', test)  # 匹配出三个到十个带有o的lemon

# 字符集

# 需求：匹配bac 或 bbc

test = 'bac | bbc | bcc | bdc | bec'

result_2 = re.findall('bac', test)

result_3 = re.findall('bbc', test)

result_4 = re.findall('b[ab]c', test)  # 字符集：匹配带有b和c之间a和b的字符

# 需求：跳过b和c之间带有的e的字符

result_5 = re.findall('b[^e]c', test)  # ^：跳过b和c之间带有e的字符

# 需求：

result_6 = re.findall('b[a-d]c', test)

result_7 = re.findall('b[^a-d]c', test)

test = '&&&A66bcc44D5ea90123456#@s1772!ACE__A-'

result_8 = re.findall('\d', test)  # \d 匹配从左到右0-9的数字，只匹配数字

result_9 = re.findall('\D', test)  # \D 匹配从左到右除了数字以外的其他所有字符

result_10 = re.findall('\w', test)  # \w 只匹配非特殊字符，即a-z、A-Z、0-9、_、汉字

result_11 = re.findall('\W', test)  # \W 只匹配特殊字符，即非字母、非数字、非汉字、非_

test = '\r\n\t\fAbc&?/68/000 0&&&  9%0@#0   25$$$4_--___a&cC%e\n\n\f\t'

result_12 = re.findall('\s', test)  # 匹配任意空白字符，等价于 [\t\n\r\f]。

result_13 = re.findall('\S', test)  # 匹配不为空字符

# 数量词


# 需求：取出完整的数字集合如 0 12 15 18 55 88

test = '%%sa%jeffresamab#2$5@22%55#66#77#888#88#0Q$%@12,15m18'

result_14 = re.findall('\d{2,3}',test)  # 数量词 {} 在括号内输入需要匹配的数位比如需要匹配1-2两位数的数字可以{1,2}

# 需求：匹配2次到N次的数字

result_15 = re.findall('\d{2,}',test)  # 打印N次后的数字只需加上逗号,

# 需求：打印 jeffrey,mable,chengxi,lemon

test = '$%@&mable*jeffrey##%43534)(#44%*123123@! !#&@$#(chengxi#((@6787(!<00<lemon>'

result_16 = re.findall('[a-z]{1,}',test)  # 注意：不能用\w因为会把数字也匹配进来

# 贪婪模式

test = 'lemon12banana34pear56lemooooooo'

result_17 = re.findall('[a-z]{4,6}?', test)  # 注意：不能用\w因为会把数字也匹配进来

# 数量词
# 贪婪：倾向于最大长度匹配
# 非贪婪：倾向于最小长度匹配，加?就好

result_18 = re.findall('lemo{1,}',test)

# 贪婪模式在整个表达式匹配成功的前提下，尽可能多的匹配
# 非贪婪模式在整个表达式匹配成功的前提下，尽可能最少的匹配

# 次数匹配

# * 表示匹配0次到n次
# + 表示匹配1次到n次
# ? 表示匹配0次到1次

test = 'jeffre123jeffrey456jeffreyyyyyyy789jeffre999'

result_19 = re.findall('jeffrey*', test)  # *号前的0次到n次

result_20 = re.findall('jeffrey+', test)  # +号前的1次到n次

result_21 = re.findall('jeffrey?', test)  # ?号前的0次到1次

# 对于?的总结，如果在数量词后面有?则进行非贪婪，如果在字符后面有?则进行0次到1次

# 定位符

# ^ 表示用来匹配字符串的边界
# $ 表示用来匹配的结尾的位置

test = 'mable #$&*#55533&$@jeffrey#@$mable&&jeffrey|chengxi'

result_22 = re.findall('[a-z]{5,7}',test)  # result_22 = re.findall('[a-z]{1,}',test)

# 需求：
# 1、 只匹配第一个mable
# 2、 匹配最后一个单词的集合

result_23 = re.findall('^[a-z]{5}', test)

result_24 = re.findall('[a-z]{7}$', test)

# 对于^的总结，在[]内加^是跳过在[]前世只匹配第一个

# 匹配组

# 需求：匹配mable

test = 'jeffreyjeffreyjeffreymablemablemarkmark'

result_25 = re.findall('(mable)', test)

result_26 = re.search('(mable){2}', test).group()

result_27 = re.findall('[mable]', test)

# 组与字符集的区别
# () 匹配一堆字符
# [] 匹配括号内的任意字符

# flags可选参数

# re.findall(规则,需要匹配的字符串,可选参数)

test = 'jeffrey&&Jeffrey&&MABLE'

result_28 = re.findall('[a-z]{1,}', test)

result_29 = re.findall('[a-zA-Z]{1,}', test)

result_30 = re.findall('jeffrey', test, re.I)

# 总结：如需匹配相同字符但不同大小写的可以添加可选参数 re.I 注意：I需要大写

# 元字符

# 匹配除了\n之外的所有字符

# 需求：匹配所有字符包括\n
test = 'mablejeffrey&\n&chengxi&\r\r\tJJJJJBBBCCCC'

result_31 = re.findall('.', test, re.S)  # re.S定义元字符.可匹配所有字符包括\n

# 需求：匹配包括大小写\n的字符集

test = 'jeffrey\n&&JEFFREY\n'

result_32 = re.findall('jeffrey.', test, re.I | re.S)  # 可选参数可使用多个需要 | 隔开，jeffrey后用.代替\n字符

# match和search函数

# re.findall(pattern,sting,flags=0) 搜索整个字符串，返回所有匹配项
# re.match(pattern,sting,flags=0) 从字符串首字符开始匹配，若字符不匹配则返回none，若匹配则返回第一个匹配对象
# re.search(pattern,sting,flags=0) 搜索整个字符串，若全部匹配，则返回none，若匹配则返回第一个匹配对象

test = 'JAAASAA664490254&&Mable===1111246706'

result_33 = re.findall('\d', test)

result_34 = re.match('\d', test)  # 返回None，因为字符串第一个不为\d数字

result_35 = re.search('\d', test)  # 循环查找，返回第一个\d数字，如一个都没找到则返回None

# 如需要查看具体匹配对象可使用group()方法

result_36 = result_35.group()

# group组匹配

# 需求
# 1、将 name is mable,im 18 years. 匹配出来
# 2、将 name,mable,years 匹配出来

test = ' My name is mable,im 18 years old.'

result_37 = re.search('My(.*)years.', test)

result_38 = re.search('My(.*)is(.*)im.*18(.*)old', test)

result_39 = result_38.groups()

test = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",test).group(0))  #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",test).group(1))  #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",test).group(2))  #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",test).group(3))  #456


# 正则替换

# re.sub(pattern,rep1,string,count=0,flags=0)
# pattern 真则表达式
# rep1 需要替换的内容，也可传入函数
# string 被替换的字符
# count 默认为零，代表全部替换
#       1、代表替换1次
#       2、代表替换两次，以此类推

# 需求：
# 1、将mable全部改为chengxi
# 2、将以下大于或等于5的全部替换为1小于5的替换为0

test = 'jeffrey mable 664490254 mable mable MABLE'

result_40 = re.sub('mable', 'chengxi', test, count=0)

# 需求2

def tranksfrom(valus):
    sum_num = valus.group()
    # print(sum_num, type(sum_num))
    if int(sum_num) >= 5:
        return '1'
    return '0'


result_41 = re.sub('\d', tranksfrom, test, count=0)

# compile函数 -- 将正则表达式转换成内部格式提高执行效率

strr = 'python666java'

pat = re.compile(r'Python', re.I)  # 模式修正术：忽略大小写 re.I

print(pat.search(strr))

# findall()函数和finditer()函数

# findall() 查找所有匹配的，装到列表中
# finditer() 查找所有匹配的内容，装到迭代器中

strr = 'hello-------------------------------' \
       '----------------------------------------' \
       '---hello------------' \
       '-----------------hello-------------' \
       '-------hello--------------'

pat = re.compile(r'hello')
data = (pat.finditer(strr))

list_ = []
for i in data:
    list_.append(i.group())
print(list_)


# split()函数和sub()函数

# split() 按照能够匹配的字符串将字符串分割后返回列表
# sub() sub方法用于替换

strr = '张三,,,李四,,,,,,,,,,王五,,,,赵六'

pat = re.compile(r',+')

data = pat.split(strr)

print(data)

strr = 'hello 123,hello 456'

pat = re.compile(r'\d+')

data = pat.sub('666', strr)

print(data)
