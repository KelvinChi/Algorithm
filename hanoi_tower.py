#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def move(n, x, y, z):
    global count
    if n == 1:
        print('%s --> %s' % (x, z))
        count += 1
    else:
        move(n - 1, x, z, y)
        print('%s --> %s' % (x, z))
        move(n - 1, y, x, z)
        count += 1


n = 4
count = 0
move(n, 'X', 'Y', 'Z')
print(count)
