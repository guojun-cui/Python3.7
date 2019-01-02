#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time     : 2019/1/2 20:45
# @Author   : CGJ
# @File     :demo3.py
a=10
print(a)
b = 3.1415926
c = round(b,3)
print(c)
string = "   acbdefgsesadfsdxadfa   "
result = string.find('s')
print(result)
print(string[0])
# replace 替换
print(string.replace('a',"AAA"))
#split() 分隔符
print(string.split('a'))
#strip 去除字符串前后的字符
print("my list :{0}".format(string))
d = string.strip()
#一定要用format这种格式
print("my list :{0}".format(d))
print("my list :{0}".format(d))
print("my list :%s" %d)
print("hello" + "world")


