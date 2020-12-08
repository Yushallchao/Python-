#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author xiao

import json

data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_obj = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_obj)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_obj)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])