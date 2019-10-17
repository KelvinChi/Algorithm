#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


def select_sort(lis, n):
    count1 = 0
    count2 = 0
    for i in range(n):
        minimum = i
        # 遍历列表，找到最小值
        for j in range(n - 1, i - 1, -1):
            count1 += 1
            if lis[j] < lis[minimum]:
                minimum = j
        # 对比如果首位不是最小值，则与最小值位交换
        if lis[i] != lis[minimum]:
            lis[i], lis[minimum] = lis[minimum], lis[i]
            count2 += 1
    print('对比次数：%s，移动次数：%s' % (count1, count2))
    return lis


lis = []
for i in range(20):
    lis.append(random.randint(1, 90))
n = len(lis)
print(select_sort(lis, n))
