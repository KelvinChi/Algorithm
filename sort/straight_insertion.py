#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


# 对比经典算法，我的因为增加了逻辑判断，所以移动的次数更少
def straight_insertion(lis, n):
    count1 = 0
    count2 = 0
    for i in range(n - 1):
        if lis[i + 1] < lis[i]:
            temp = lis[i + 1]
            lis.pop(i + 1)
            for j in range(i, -1, -1):
                count1 += 1
                if temp < lis[0]:
                    lis.insert(0, temp)
                    count2 += 1
                    break
                elif temp >= lis[j]:
                    lis.insert(j + 1, temp)
                    count2 += 1
                    break
    print('对比次数：%s，移动次数：%s' % (count1, count2))
    return lis



lis = []
# lis = [90, 34, 14, 14, 46, 42, 20, 49, 58, 54]
for x in range(20):
    lis.append(random.randint(1, 90))
n = len(lis)
print(straight_insertion(lis, n))
