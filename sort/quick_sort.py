#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random


# 下边是我自己写的，似乎还是需要很多步数
# def quick_sort(lis):
#     global count
#     if len(lis) > 2:
#         smaller, larger = [], []
#         m = len(lis) // 2
#         for i in range(len(lis)):
#             count += 1
#             if i == m:
#                 continue
#             smaller.append(lis[i]) if lis[i] <= lis[m] else larger.append(lis[i])
#         smaller.append(lis[m]) if len(smaller) <= len(larger) else larger.append(lis[m])
#         left = quick_sort(smaller)
#         right = quick_sort(larger)
#         lis = left + right
#     return lis


def mid_picker(lis):
    lis.remove(max(lis))
    lis.remove(min(lis))
    return lis[0]

# 下边是百度复制的，总体思路和我自己写的没有什么区别，只是有几个地方他更简洁，加油吧！
def quick_sort(data):
    global count
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        # 优化算法，选取较好的中间值
        mid = mid_picker([data[0], data[len(data)//2], data[-1]])
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值，喵啊
        for num in data:
            count += 1
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right) # 喵喵喵
    else:
        return data


count = 0
lis = []
# lis = [37, 28, 88, 35, 53, 27, 16, 31, 89, 4]
for i in range(200):
    lis.append(random.randint(1, 90))
print(quick_sort(lis))
print('对比、移动次数：%s' % count)
