#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


# 经典递归实现，整体非常简洁，当以此为目标！
def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur + 1)


if __name__ == '__main__':
    queen([None]*8)