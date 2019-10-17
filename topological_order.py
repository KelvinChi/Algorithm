#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def topological_order(lis, n):
    # 把出度为0的点都放一起
    part1, result_index = [], []
    for i in lis:
        if len(i) == 1:
            part1.append(i)
            result_index.append(lis.index(i))
    # 下边的删除过程应该可以优化，先不考虑
    for j in range(len(result_index) - 1, -1, -1):
        lis.pop(result_index[j])
    # 下边是判断是否节点只有入度没有出度
    head = [i[0] for i in lis]
    count, temp = 0, 0
    part2 = []
    while len(lis) > 0:
        for x in head:
            for y in lis:
                if x in y:
                    count += (1 + y.index(x))
                    temp = y
            if count == 1:
                part2.append(temp)
                lis.remove(temp)
            count = 0
    result = part2 + part1
    return [x[0] for x in result]


if __name__ == '__main__':
    # 构造邻接表，第一个数字表示自身，后边几个表示出度分别指向的位置
    A = [1, 2, 3, 4]
    B = [2]
    C = [3, 6, 7, 9, 10]
    D = [4, 8]
    E = [5]
    F = [6]
    G = [7]
    H = [8]
    I = [9]
    J = [10, 7, 11]
    K = [11, 12]
    L = [12]
    M = [13, 4, 14]
    N = [14, 2, 3, 15]
    O = [15, 5]
    lis = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]
    n = len(lis)
    print(topological_order(lis, n))












