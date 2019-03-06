#!/usr/bin/python
# -*- coding:utf-8 -*-
import time, threading
# 创建一个继承thread的类

from threading import Thread
from queue import Queue
import traceback


class tWork(Thread):
    def __init__(self, event=None, tQueue=None, i=0):
        Thread.__init__(self)
        self.event = event          # 事件触发 用于线程间通信
        self.tQueue = tQueue          # 队列
        self.threadName = self.getName()

    def run(self):  # 线程启动后自动运行run方法
        print('run')
        while (True):
            self.event.wait()   # 线程进入阻塞，直到获取到触发信号
            self.event.clear()
            try:
                while not self.tQueue.empty():
                    try:
                        pushMsg = self.tQueue.get_nowait()
                    except Exception as e:
                        pushMsg = ''

                    self.printMsg(pushMsg)
            except Exception as inst:
                if(inst):
                    self.printMsg(self.threadName+" error: "+inst)
                self.printMsg(traceback.print_exc())
                self.printMsg(pushMsg)

    def printMsg(self, pushMsg):
        print(pushMsg)


# 创建队列
tQueue = Queue()
# 创建事件
tEvent = threading.Event()  # 通过event进行线程间通信，与使用锁进入阻塞来进行通信的区别
threadSer = tWork(event=tEvent, tQueue=tQueue, i=0)
# 启动线程
threadSer.start()


while True:
    pushMsg = "some data"
    tQueue.put(pushMsg)         # 写入队列
    tEvent.set()       # 触发event事件

    time.sleep(10)


