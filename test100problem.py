#!/usr/bin/python
# -*- coding: UTF-8 -*-

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