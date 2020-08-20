import queue

# Queue是 python标准库中的线程安全的实现
# 提供了一个适用于多线程绵程的先进先出的数据结构
# 即队列，用来在生产者和消费者线程之间的信息传递
# 对于资源，加锁是个重要的环节
# 因为 python原生的11st，dict等，都是非线程安全的
# 而 Queue，是线程安全的，因此在满足使用条件下，建议使用队列。

# 创建队列
q = queue.Queue(maxsize=20)

for i in range(1,21):
    q.put(i)


while not q.empty():
    print(q.get())

print('已取完！')