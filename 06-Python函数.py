#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author xiao
#自定义函数
def myFoo(str):
    print(str)
    return


myFoo("你好")


def changeInt(a):
    a = 10
    return a


b = 2
changeInt(b)
print(b)
print(changeInt(b))


# 默认参数
def defineArgs(name, age=18):
    print("Name:%s\nAge:%d" % (name, age))
    return


defineArgs("mike", 28)
defineArgs(age=28, name="mike")
defineArgs(name="xiao")

# 不定长参数 加了星号（*）的变量名会存放所有未命名的变量参数。
def printinfo(*vartuple):
    "打印任何传入的参数"
    print("输出: ")
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, "ddd")

#匿名函数 使用 lambda 来创建匿名函数。
sum = lambda arg1, arg2: arg1 + arg2

print("调用lambda匿名函数：",sum(10,21))


