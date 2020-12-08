# -*- coding: utf-8 -*-
'''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
counter = 100 #整型变量
miles = 1000.01 #浮点型变量
name = 'yuxiaochao' #字符串,title标题化字符串

print(counter)
print(miles)
print(name.title())

#同时为多个变量赋值
a,b,c = 1,0.2,'xiao'

#1、Number数字）
#Python3 支持 int、float、bool、complex（复数）
a,b,c,d = 1,0.2,True,4+3j
print(type(a),type(b),type(c),type(d))
#运算
#混合计算时，Python会把整型转换成为浮点数
a = 5+4
print('加法运算：%d'%(a))#%d格式化整数
a = 105.04-2
#-：左对齐; +：在转换值之前加上正负号;
#0表示占位符，.之后数字表示保留位数
print('减法运算：%-0.1f'%(a))#%f格式化浮点数字，可指定小数点后的精度
a = 3*4
print('乘法运算：%d'%(a))
a = 6/4
print('除法，得到一个浮点数：%0.2f'%(a))
a = 6//4
print('除法，得到一个整数：%d'%(a))
a = 17%3
print('取余：%d'%(a))
a = 2**5
print('乘方：%d'%(a))

#2、String（字符串）
#Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误
word = 'Python'
print('字符串大小：'+str(len(word))+',第一个位置：'+word[0])
word = "你好!"
print('字符串大小：'+str(len(word))+',第一个位置：'+word[0])
#字符串大小表示下标与字符串长度无关
size = int((len(word.encode('utf-8')) - len(word))/2 + len(word))
print("size=",size)

#以下单独练习
#3、List（列表）
car_list=["A","B","C","1"]
dir(car_list)

for value in range(2):
    print(value)
for value in range(0,2):#两种写法一致，不包含第二个数
    print(value)
for value in range(1,11,2):#1开始+2，并小于11
    print(value)
l=[]
for value in range(3,30,3):
    l.append(value)
print(l)
#将一个列表存储到另一个列表
l2=l[:]
#这是不行的，两个变量是指向同一个列表
#l2=l
l.append(30)
print(l2)

#4、Tuple（元组）
#元组的元素不可变
t1 = (1,2,{'k1':'v1'})
#del t1[0]
#t1[2] = 123
#元组元素的元素可变
t1[2]['k1'] = 2
print(t1)
#5、Set（集合）
#6、Dictionary（字典）
#键-值对
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',#加逗号，为以后下一行添加键值对做好准备

}
for key,value in user_0.items():
    print("\nKey："+key)
    print("\nValue："+value)


#类型转换
'''
int(x [,base]) 将x转换为一个整数

float(x) 将x转换到一个浮点数

complex(real [,imag]) 创建一个复数

str(x) 将对象 x 转换为字符串

repr(x) 将对象 x 转换为表达式字符串

eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s) 将序列 s 转换为一个元组

list(s) 将序列 s 转换为一个列表

set(s) 转换为可变集合

dict(d) 创建一个字典。d 必须是一个 (key, value)元组序列。

frozenset(s) 转换为不可变集合

chr(x) 将一个整数转换为一个字符

ord(x) 将一个字符转换为它的整数值

hex(x) 将一个整数转换为一个十六进制字符串

oct(x) 将一个整数转换为一个八进制字符串
'''

