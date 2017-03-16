#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import time
import string

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

#007
#题目：将一个列表的数据复制到另一个列表中。
'''
a = [4,5,6]
b = []
print a
print b
b = a[:]
print a
print b
'''

#008
#输出 9*9 乘法口诀表。
'''
for i in range(1,10):
    for j in range(1,i+1):
        string = "%d * %d = %d" % (i, j, i * j)
        print string,
    print
'''

#009
#暂停一秒输出
'''
for i in range(10):
    time.sleep(1)
    print i
'''

#010
#暂停一秒输出，并格式化当前时间
'''
for i in range(10):
    time.sleep(1)
    print time.asctime()
'''

#011
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？

#012
#判断101-200之间有多少个素数，并输出所有素数。
'''
def isSuShu(count):
    for index in range(2,count):
        if(count%index == 0):
            return False
    return True
sum = 0
for index in range(101,200):
    if(isSuShu(index)):
        sum += 1
        print index
print sum
'''

#013
#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
'''
for index in range(100,1000):
    ge = index % 10
    shi = index/10%10
    bai = index/100
    if ge**3 + shi**3 + bai**3 == index:
        print index
'''

#014
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
list = []
def fenjie(count):
    for index in range(2,count+1):
        if count %index == 0:
            print index
            list.append(index)
            fenjie(count/index)
            return
num = int(raw_input("请输入整数:"))
if num < 2:print ("输入错误");exit()
fenjie(num)
str = "%d="%(num)
for index in range(len(list)):
    if index == 0 :
        str = str + "%d"%(list[index])
    else:
        str = str + "*" +"%d"%(list[index])
print str
'''

#015
#利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
'''
num = int(raw_input("请输入整数:"))
if num < 0 or num > 100:
    print "输入有误"
    exit()
elif num >= 90:
    print "A"
    exit()
elif num >= 60:
    print "B"
    exit()
else:
    print "C"
    exit()
'''

#016
#利用

#017
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
'''
str = raw_input("请输入字符串:")
letters = 0
space = 0
digit = 0
other = 0
for c in str:
    if c.isalpha():
        letters +=1
    elif c.isspace():
        space +=1
    elif c.isdigit():
        digit +=1
    else:
        other +=1
print str
print "letters = %d,space = %d,digit = %d,other = %d"%(letters,space,digit,other)
'''

#018
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
#例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
'''
def sameNum(a,digit):
    sum = 0
    for index in range(digit):
        sum += a*(10**index)
    return sum

a = int(raw_input("请输入数字a:"))
num = int(raw_input("请输入数字个数num:"))
sum = 0
for index in range(1,num+1):
    sum += sameNum(a,index)
print sum
'''

#019
#一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
def yinzi(num):
    list = []
    for index in range(1,num):
        if num%index == 0:
            list.append(index)
    return list

for index in range(1,1000):
    li = yinzi(index)
    sum = 0;
    for i in li:
        sum += i
    if sum == index:
        print index
        print li
'''

#020
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？




#021
#利用

#022
#利用

#023
#利用




































