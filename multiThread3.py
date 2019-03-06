#!/usr/bin/python
# -*- coding:utf-8 -*-

import time, threading
from threading import Thread


#使用锁来协调线程的并发执行

num = 0
lock = threading.Lock()

class tWork(Thread):
    def __init__(self,step=0):
        Thread.__init__(self)
        self.step = step

    def run(self):
        global num
        for i in range(10):
            # 先要获取锁:
            lock.acquire()
            try:
                time.sleep(1)
                # 放心地改吧:
                print(str(num) + '+'+str(self.step))
                num = num+self.step
                print(str(num) + '-' + str(self.step))
                num = num-self.step


            finally:
                # 改完了一定要释放锁:
                lock.release()
                # num


threadSer = tWork(5)
threadSer2 = tWork(8)

threadSer.start()
threadSer2.start()

# threadSer.join()
# threadSer2.join()
# 是不是用join 主线程最后都会阻塞等待子线程
for i in range(10):
    print('why')

