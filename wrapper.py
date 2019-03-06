#/usr/bin/python
# -*- coding:utf-8 -*-
import logging



def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging    # 装饰器的逻辑是，把foo函数传入的装饰器函数中去，装饰器函数返回一个可执行的wrapper函数，wrapper函数里面再执行foo函数
def foo():
    print("i am foo")


foo()