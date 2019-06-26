import threading, time, os, queue

# 把线程类当做元素添加到队列内。实现方法比较糙，每个线程使用后就被抛弃，一开始就将线程开到满性能不佳

class ThreadPool(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._q = queue.Queue(self.maxsize)
        for i in range(self.maxsize):
            self._q.put(threading.Thread)

    def getThread(self):
        return self._q.get()

    def addThread(self):
        self._q.put(threading.Thread)


def fun(num, p):
    print('this is thread [%s]' % num)
    time.sleep(1)
    p.addThread()


if __name__ == '__main__':
    pool = ThreadPool(2)
    for i in range(103):
        t = pool.getThread()
        a = t(target=fun, args=(i, pool))
        a.start()
