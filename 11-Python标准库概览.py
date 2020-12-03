#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author xiao

#1、操作系统接口
import os
print(dir(os))
#文件通配符
import glob
print(glob.glob("*.py"))
#命令行参数
import sys
print(sys.argv)

#字符串正则匹配
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

#数学
import math
print(math.cos(math.pi / 4))

#访问 互联网

from urllib.request import urlopen
for line in urlopen('https://www.runoob.com/python3/python3-stdlib.html'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    #print(line)

#日期和时间
import  datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
import time
print("当前时间： ",time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time())))
#常用时间处理方
#今天
today = datetime.date.today()
#昨天
yesterday = today - datetime.timedelta(days=1)
#上个月
last_month = today.month - 1 if today.month - 1 else 12
#当前时间戳
import time
time_stamp = time.time()
print(time_stamp)
#时间戳转datetime
datetime.datetime.fromtimestamp(time_stamp)
#datetime转时间戳
int(time.mktime(today.timetuple()))
#datetime转字符串
today_str = today.strftime("%Y-%m-%d %H:%M:%S")
print(today_str)
#字符串转datetime

#补时差
today + datetime.timedelta(hours=8)
