#默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
# -*- coding: utf-8 -*-
#!/usr/bin/python3
# coding=utf-8
 
# 第一个注释
print ("Hello, Python3!") # 第二个注释

'''
第三注释

'''
 
"""
第四注释
"""

if True:
    print ("True")
    print("Hello, Python3! again")
else:
    print ("False")


str = 'Runoob'#python中单引号和双引号使用完全相同 (''="")
print(str)
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符,从右往左以-1开始
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

p = input()
print(p)

#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys;x = 'runoob'; sys.stdout.write(x + '\n')

## 不换行输出在变量末尾加上 end=""
print(str, end="")
print(str, end="")


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path