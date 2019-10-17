#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


def shell_sort(lis, n):
    global count1, count2
    gap = n
    while gap >= 1:
        gap = gap // 2
        for i in range(gap, n):
            if lis[i] < lis[i - gap]:
                temp = lis[i]
                for j in range(i - gap, -1, -1):
                    count1 += 1
                    if lis[j] > temp:
                        count2 += 1
                        lis[j + gap] = lis[j]
                        lis[j] = temp
                        if gap != 1:
                            break
    return lis


if __name__ == '__main__':
    count1 = 0
    count2 = 0
    lis = []
    # lis = [53, 73, 56, 32, 1]
    for x in range(10):
        lis.append(random.randint(1, 99))
    n = len(lis)
    print(shell_sort(lis, n))
    print('对比次数：%s，移动次数：%s' % (count1, count2))
