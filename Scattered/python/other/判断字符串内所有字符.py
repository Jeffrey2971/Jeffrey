# coding: utf-8

import string
from collections import namedtuple


def str_count(s):
    '''找出字符串中的中英文、空格、数字、标点符号个数'''

    count_en = count_dg = count_sp = count_zh = count_pu = 0
    s_len = len(s)
    for c in s:
        if c in string.ascii_letters:
            count_en += 1
        elif c.isdigit():
            count_dg += 1
        elif c.isspace():
            count_sp += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    total_chars = count_zh + count_en + count_sp + count_dg + count_pu
    if total_chars == s_len:
        return namedtuple('Count', ['total', 'zh', 'en', 'space', 'digit', 'punc'])(s_len, count_zh, count_en, count_sp, count_dg, count_pu)
    else:
        print('Something is wrong!')
        return None
    return None


s = '上面是引用了官网的介绍，意思就是说 TensorBoard 就是一个方便你理解、调试、优化 TensorFlow 程序的可视化工具，你可以可视化你的 TensorFlow graph、学习参数以及其他数据比如图像。'
count = str_count(s)
print(s, end='\n\n')
print('该字符串共有 {} 个字符，其中有 {} 个汉字，{} 个英文，{} 个空格，{} 个数字，{} 个标点符号。'.format(count.total, count.zh, count.en, count.space, count.digit, count.punc))

