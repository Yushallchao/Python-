#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author xiao

#捕捉异常可以使用try/except...else语句。
try:
    file = open("test.txt","r")#r读，w写
    file.write("这是一个测试文件，用于测试异常！")
except IOError:
    print("Error:没有找到文件！")
else:
    print("内容写入成功！")
    file.close()

#ry-finally 语句无论是否发生异常都将执行最后的代码。
finally:
    print('finally这句，无论异常是否发生都会执行。')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,0)
divide(2,1)