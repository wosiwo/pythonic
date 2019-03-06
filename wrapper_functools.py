#/usr/bin/python
# -*- coding:utf-8 -*-

from functools import wraps
def logged(func):
    @wraps(func)    #使用@wraps 将原函数f的元信息传入装饰器函数with_logging
    def with_logging(*args, **kwargs):
        print func.__name__      # 输出 'f'
        print func.__doc__       # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x