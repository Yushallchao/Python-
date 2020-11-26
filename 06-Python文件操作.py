#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
#1、创建文件，mknod只在linux存在
#os.mknod("test.txt")
#windows下以追加的方式open文件就会自动创建
file = open("test.txt","a+")#读写，追加
print("文件名: ", file.name)
print("是否已关闭 : ", file.closed)
print("访问模式 : ", file.mode)
#写
#file.write("你好\nPython\n")
#读
file = open("test.txt","r+")#读写
print("文件读取：%s"%(file.read()))
# 查找当前位置
path = file.tell()
print(path)
file.close()