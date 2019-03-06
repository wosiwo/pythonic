#!/usr/bin/python
# -*- coding:utf-8 -*-

import time, threading
# from threading import Thread
import random
# 条件变量


from queue import Queue

queue = Queue(10)       #线程安全队列

con = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if queue.qsize() > 100:
                    con.wait()
                else:
                    elem = random.randrange(100)
                    queue.put(elem)
                    print("Producer a elem {}, Now size is {}".format(elem, queue.qsize()))
                    time.sleep(random.random())
                    con.notify()
                con.release()


class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if queue.qsize() < 0:
                    con.wait()  # 释放锁 与release的区别？
                else:
                    elem = queue.get()
                    print("Consumer a elem {}. Now size is {}".format(elem, queue.qsize()))
                    time.sleep(random.random())
                    con.notify()    # 唤醒其他线程，但没有释放锁
                con.release()   # 释放锁，这时候其他线程才能开始执行


def main():
    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()
