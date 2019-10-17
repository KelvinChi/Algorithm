#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return Merge(left, right)


def Merge(left, right):
    global count
    # 注意下边这种赋值方法，常用
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        count += 1
    result += list(left[l:])
    result += list(right[r:])
    return result


count = 0
lis = []
for i in range(10):
    lis.append(random.randint(1, 90))
n = len(lis)
print(merge_sort(lis))
print('对比、移动次数：%s' % count)
