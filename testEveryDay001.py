#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

#获取length位激活码
def getCodeNum(length):

    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    char = ""
    for dex in range(0, length):
        index = random.randint(0, 35)
        char = char + str[index]
    return char

#打印count个length长度的激活码
def printCode(count,length):

    list = []
    # 将激活码放入list中
    while len(list) != count:
        tmp = getCodeNum(length)
        flag = 0
        for code in list:
            if (tmp == code):
                flag = 1
                break
        if (flag == 0):
            list.append(tmp)

    for index in list:
        print index

#打印激活码
printCode(100,16)