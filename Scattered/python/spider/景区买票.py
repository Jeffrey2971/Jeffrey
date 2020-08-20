import threading
import time
num = 100

# 买票
lock = threading.Lock()

def sele(name):
    lock.acquire()
    global num
    if num > 0:
        num -= 1
    print(name + '窗口卖出一张,还剩：' + str(num) + '张！')
    lock.release()
# 售票窗口（两个线程表示）


while 1 == 1:
    if num > 0:
        ta = threading.Thread(target=sele, args=('A窗口',))
        tb = threading.Thread(target=sele, args=('B窗口',))

        ta.start()
        tb.start()
        ta.join()
        tb.join()

    else:
        break

print('已售空！',)
