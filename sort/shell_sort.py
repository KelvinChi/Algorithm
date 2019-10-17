#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


def straight_insertion(lis, n):
    global count1, count2
    for i in range(n - 1):
        # 对比前后两个，如果后小于前一个，则复制后者且弹出，在前部找相应位置插入
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
    return lis


# 自己写的好像有bug，超过20记录的表会递归超出，烂啊，还是学习经典算法好
def shell_sort(lis, n):
    global count1, count2
    m = n // 2
    # 把原表一分为二，对比前后两表相同位置记录，小的放前面，相当于给直接插入排序做预处理
    for i in range(m):
        count1 += 1
        if lis[:m][i] > lis[m:][i]:
            count2 += 1
            lis[i], lis[m + i] = lis[m + i], lis[i]
    # 递归实现直到表元素只能两两对比
    if m != 2:
        shell_sort(lis[:m], m)
        shell_sort(lis[m:], n - m)
    return lis


count1 = 0
count2 = 0
lis = []
# lis = [90, 34, 14, 14, 46, 42, 20, 49, 58, 54]
for x in range(20):
    lis.append(random.randint(1, 90))
n = len(lis)
print(lis)

new_lis = shell_sort(lis, n)
print(new_lis)

print(straight_insertion(new_lis, n))
print('对比次数：%s，移动次数：%s' % (count1, count2))
