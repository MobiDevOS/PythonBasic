# -*- coding: UTF-8 -*-
from queue import Queue
from threading import Thread
import time

isRead = True


def write(q):
    # 写数据进程
    for value in ['两点水', '三点水', '四点水']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)
        time.sleep(1)


def read(q):
    # 读取数据进程
    while isRead:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t1.daemon = True

    t2 = Thread(target=read, args=(q,))
    t2.daemon = True
    t1.start()
    t2.start()
