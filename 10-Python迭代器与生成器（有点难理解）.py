#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author xiao

#迭代器是一个可以记住遍历的位置的对象。
#迭代器有两个基本的方法：iter() 和 next()。

list=[1,2,3,4]
it = iter(list) #创建迭代器对象
print(next(it))
print(next(it))

for i in it:
    print(str(i),end=" ")

print("")

import sys

#使用 yield 的函数被称为生成器（generator）
#生成器是一个返回迭代器的函数
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()