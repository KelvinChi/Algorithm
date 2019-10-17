#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from prim import graph_with_weight
import numpy as np


def floyd(matrix, path, n):
    A = matrix[:]
    for i in range(n):
        for j in range(n):
            if matrix[i, j] != 1 << 9 and matrix[i, j] != 0:
                path[i][j] = i

    print('init matrix & path:\n')
    print(A, '\n\n', path)
    print('~' * 40)

    # 代表通过点0各顶点的最短距离多少，如果有无穷大更新为数字，则说明把0作为中转有可以使i到j
    # 假如原先一个大的数字变小，说明直达比中转更慢
    # 如果原先无穷大，在0中转后变成10，加上中转1后它变成8，说明通过中转1、2更小
    # path代表当前点前一个中转点位置
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i, k] + A[k, j] < A[i, j]:
                    A[i, j] = A[i, k] + A[k, j]
                    path[i][j] = path[k][j]

    print('result matrix & path:\n')
    print(A, '\n\n', path)


if __name__ == '__main__':
    lis = [('V0', 'V1', 1), ('V0', 'V2', 5), ('V1', 'V2', 3), ('V1', 'V3', 7),
           ('V1', 'V4', 5), ('V2', 'V4', 1), ('V2', 'V5', 7), ('V3', 'V4', 2),
           ('V3', 'V6', 3), ('V4', 'V5', 3), ('V4', 'V6', 6), ('V4', 'V7', 9),
           ('V5', 'V7', 5), ('V6', 'V7', 2), ('V6', 'V8', 7), ('V7', 'V8', 4)]
    dic = {}
    for j in graph_with_weight(lis)[0]:
        dic[graph_with_weight(lis)[0].index(j)] = j
    matrix = graph_with_weight(lis)[1]
    n = len(matrix)
    path = np.zeros([n, n])

    print('~' * 40)
    print(matrix)
    print('~' * 40)
    floyd(matrix, path, n)
