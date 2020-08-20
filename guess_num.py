def start():
    import random
    random_num = random.randint(1, 9)
    items = 3
    while items > 0:  #
        enter = int(input('请输入 1-9 的正整数：'))
        if enter > random_num:
            print('大了')
        elif enter < random_num:
            print('小了')
        else:
            print('恭喜你猜对了，正确答案是：' + str(random_num))
            break  # 这里避免次数用完后输入正确不跳出
        items -= 1
        if items == 0:
            print('三次机会都没有猜对，正确答案是：' + str(random_num))
            break


if __name__ == '__main__':
    start()
