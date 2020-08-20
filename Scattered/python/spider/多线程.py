import threading
import time

def run(name):
    print(name, '线程执行了！')
    time.sleep(10)

t1 = threading.Thread(target=run, args=('This is T1',))
t2 = threading.Thread(target=run, args=('This is T2',))

t1.start()
t2.start()

t1.join()
t2.join()

print('执行结束')
