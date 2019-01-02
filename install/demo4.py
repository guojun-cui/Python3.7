#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time     : 2019/1/2 21:55
# @Author   : CGJ
# @File     :demo4.py
def add(string):
    total = 0
    numbers = []
    numbers += string.split("+")
    for num in numbers:
        total += int(num.strip())
    print("{0} = {1}".format(string, total))


def reduce(string):
    result = 0
    numbers = []
    numbers += string.split("-")
    result = int(numbers[0].strip())
    numbers.pop(0)
    for num in numbers:
        result -= int(num.strip())
    print("{0} = {1}".format(string, result))


def ride(string):
    total = 1
    numbers = []
    numbers += string.split("*")
    for num in numbers:
        total *= int(num.strip())
    print("{0} = {1}".format(string, total))


def divising(string):
    numbers = []
    numbers += string.split("/")
    result = int(numbers[0])
    numbers.pop(0)
    for num in numbers:
        result /= int(num.strip())
    print("{0} = {1}".format(string, result))


if __name__ == '__main__':
    print("######################################################")
    print("#####################计算机##########################")
    print("######################################################")
    print("1：+")
    print("2：-")
    print("3：*")
    print("4：/")
    method = input("please input number(1/2/3/4):")
    if method == "1":
        string = input("请输入你的表达式：")
        add(string)
    elif method == "2":
        string = input("请输入你的表达式：")
        reduce(string)
    elif method == "3":
        string = input("请输入你的表达式：")
        ride(string)
    elif method == "4":
        string = input("请输入你的表达式：")
        divising(string)
    else:
        print("error")
