#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import random
from algorithm import nodefun


def heap_sort(root):
    global count, temp
    if not root:
        return
    heap_sort(root.left)
    heap_sort(root.right)
    if root.left and root.left.value < root.value:
        count += 1
        root.value, root.left.value = root.left.value, root.value
    if root.right and root.right.value < root.value:
        count += 1
        root.value, root.right.value = root.right.value, root.value
    temp = min(temp, root.value)
    return temp


count = 0
lis = []
# lis = [90, 34, 14, 10, 46, 42, 20]

t = nodefun.Tree()
for x in range(10):
    random_int = random.randint(1, 90)
    t.add(random_int)
    lis.append(random_int)
n = len(lis)
print(lis)

result = []
t.tree_structure(t.root)

new_lis = []
print('~' * 30)

while len(result) < n:
    temp = float('inf')
    value = heap_sort(t.root)
    result.append(value)
    count += 1
    t.root.value, t.root.right.value = t.root.right.value, 1 << 10
print(result)
print('对比、移动次数：%s' % count)

