#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

#001
'''
arr = [1,2,3,4]
tmp = 0;
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if(i == j or j == k or i == k):
                continue;
            else:
                tmp += 1
                print arr[i],arr[j],arr[k]
print  tmp
'''

#002
'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

str = raw_input("请输入：")
num = eval(str)
retur = 0;
if (num > 0 and num <= 10):
    retur = num * 0.1
elif (num > 10 and num <= 20):
    retur = 10 * 0.1 + (num - 10) * 0.075
elif (num > 20 and num <= 40):
    retur = 10 * 0.1 + 10 * 0.075 + (num - 20) * 0.05
elif (num > 40 and num <= 60):
    retur = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (num - 40) * 0.03
elif (num > 60 and num <= 100):
    retur = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (num - 60)* 0.015
else:
    retur = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (num - 100)* 0.01

print "净利润：%.5f"%retur
'''

#003

#题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''
for num in range(10000):
    i = math.sqrt(num + 100)
    j = math.sqrt(num + 268)
    if(j == int(j)) and (i == int(i)):
        print i
        print j
        print num
        break
'''

#004
#输入某年某月某日，判断这一天是这一年的第几天？
'''
def isYun(year):
    #2月闰年29 平年28
    if(year % 4 == 0):
        return True
    else:
        return False
def daysFromMouth(year,mouth):
    if(mouth == 1 or mouth == 3 or mouth == 5 or mouth == 7 or mouth == 8 or mouth == 10 or mouth == 12):
        return 31
    elif(mouth == 4 or mouth == 6 or mouth == 9 or mouth == 11):
        return 30
    else:
        if(isYun(year)):
            return 29
        else:
            return 28
year = eval(raw_input("请输入年"))
if(year <= 0):
    print "年输入错误"
    exit()

mouth = eval(raw_input("请输入月"))
if(mouth <= 0 or mouth > 12):
    print "月输入错误"
    exit()

day = eval(raw_input("请输入日"))
if(day <= 0 or day > 31):
    print "日输入错误"
    exit()

num = 0
for index in range(1,mouth):
    num += daysFromMouth(year,mouth)
num += day
print "这是%d年第%d天"%(year,num)
'''

#005
#输入三个整数x,y,z，请把这三个数由小到大输出
'''
arr = []
for index in range(3):
    tmp = eval(raw_input("int:"))
    arr.append(tmp)
arr.sort(reverse=False)#递增
print arr
arr.sort(reverse=True)#递减
print arr
'''

#006
#斐波那契数列

'''
#fun1

def fibonacci_List(index):
    if(index == 0 or index == 1):
        return 1
    else:
        return fibonacci_List(index-1) + fibonacci_List(index-2)
list = []
for index in range(10):
    list.append(fibonacci_List(index))
print list
'''

'''
#fun2

list = [1,1]
for index in range(2,10):
    list.append(list[index -1] + list[index -2])
print list
'''








