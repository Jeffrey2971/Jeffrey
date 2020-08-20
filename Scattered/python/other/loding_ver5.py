# My first python object,restructure 5 times,finish at 2019/11/29

# 需求：
#
#
#
#
#
#
#
#
#
#

import os
import time

path = 'C:\\Users\\hongj\\Desktop\\test.txt'  # 家 path
# path = 'C:\\Users\\28158\\Desktop\\test.txt'  # 宿舍 path
# path = 'C:\\Users\\Administrator.USER-20191115PO\\Desktop\\test.txt'  # 公司
result = os.path.exists(path)

if result is True:
    pass
else:
    def preset_long():  # 长度上下限
        global preset_user_longest, preset_user_minimum, preset_code_longest, preset_code_minimum  # 设定为全局变量
        preset_user_longest = 8  # 账户长度上限
        preset_user_minimum = 5  # 账户长度下限
        preset_code_longest = 16  # 密码长度上限
        preset_code_minimum = 8  # 密码长度下限
        return

    def test_long(u, c):

        user_long = len(u)  # 计算帐号长度
        code_long = len(c)  # 计算密码长度

        if user_long > preset_user_longest:
            print('帐号输入长度不得大于八位数。')
            exit()
        elif code_long > preset_code_longest:
            print('密码输入长度不得超过十六位数。')
            exit()
        elif user_long < preset_user_minimum:
            print('帐号输入长度不得小于五位数。')
            exit()
        elif code_long < preset_code_minimum:
            print('密码输入长度不得小于八位数。')
            exit()
        else:
            return

    def test_code_safe(c):
        q = 0
        for item in c:
            if (item > "a" and item < "z") or (item > "A" and item < "Z"):
                q += 1
        if q <= 3:
            print('请输入三位或以上任意大小写的字母。')
            exit()
        else:
            return

    register_user = (input('请输入账号：'))
    if register_user == '':
        print('账号输入不能为空。')
        exit()
    else:
        register_code = (input('请输入密码：'))
        if register_code == '':
            print('密码输入不能为空。')
            exit()
        else:
            preset_long()
            test_long(register_user, register_code)
            test_code_safe(register_code)

            data = ('User：' + register_user + '\nCode：' + register_code)
            with open(path, 'a')as f:
                f.write(data)
            print('注册成功，请重新登录。')
            exit()



def contrast(_items=6, _time=180, _end=3):
    f = open(path)
    count = len(f.readlines())
    f = open(path)
    a = {}
    for line, i in zip(f, range(count)):
        a[i] = line.strip('\n')
        # a[0] = user a[1] = code
    while _items > 0:
        loding_user = (input('请输入登录帐号：'))
        if loding_user == '':
            print('帐号输入不能为空。')
        else:
            loding_user = 'User：' + loding_user
            _list = [loding_user]
            loding_code = (input('请输入登入密码：'))
            if loding_code == '':
                print('密码输入不能为空。')
            else:
                loding_code = 'Code：' + loding_code
                _list = [loding_user, loding_code]
                if (_list[0] == a[0]) and (_list[1] == a[1]):
                    print('登录成功')
                    exit()
                else:
                    _items -= 1
                    if _items <= 3:
                        print('您输入的错误过多，程序将暂停您的操作，请在 ' + str(_time) + ' 秒后重试，您还有 ' + str(_end) + ' 次重试机会。')
                        _end -= 1
                        if _end == 0:
                            print('出于安全考虑，您的电脑将在60秒后关机，请及时做好备份操作。')
                            os.system('shutdown -s -t 60')
                            exit()
                        time.sleep(_time)
                        _time += 180  # tmp
                    else:
                        print('帐号或密码输入错误，请重新输入。')
                        print(_items, _time, _end)


contrast()
