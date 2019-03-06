#!/usr/bin/python
# -*- coding:utf-8 -*-

import time, threading
# from threading import Thread

mutex = threading.RLock()  # 可以重入锁


class MyThread(threading.Thread):

    def run(self):
        if mutex.acquire(1):
            print("thread {} get mutex".format(self.name))
            time.sleep(1)
            mutex.acquire()
            mutex.release()
            mutex.release()


def main():
    print("Start main threading")

    threads = [MyThread() for i in range(2)]
    for t in threads:
        t.start()

    print("End Main threading")
