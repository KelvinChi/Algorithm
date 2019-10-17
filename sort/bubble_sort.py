#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


def bubble_sort(lis, n):
    flag = 1
    count1 = 0
    count2 = 0
    # 设定循环次数
    for i in range(n - 1):
        # 判断倒数第二次遍历，如果已经不需要调整了，则直接退出循环
        if flag:
            flag = 0
        # 从后往前依次对比
            for j in range(n - 1, i, -1):
                count1 += 1
                if lis[j - 1] > lis[j]:
                    lis[j - 1], lis[j] = lis[j], lis[j - 1]
                    count2 += 1
                    flag = 1
    print('对比次数：%s，移动次数：%s' % (count1, count2))
    return lis


lis = []
for i in range(10):
    lis.append(random.randint(1, 90))
n = len(lis)
print(bubble_sort(lis, n))

