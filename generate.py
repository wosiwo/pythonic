#/usr/bin/python
# -*- coding:utf-8 -*-

# 列表推导
L = [x * x for x in range(10)]

# generate生成器 ，生成器保存的是算法，而不是提交把逻辑执行完
g = (x * x for x in range(10))
print(g)
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：

print(next(g))
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

for n in g: # 使用for循环，因为generator也是可迭代对象
    print(n)

#所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#调用函数遇到yield就会终端函数执行，并返回，再次调用就会从yield后继续执行
#我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
# 通yield是的函数变成的generator，不能同个迭代直接拿到返回值
g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break