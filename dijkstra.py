#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from prim import graph_with_weight


def dijkstra(matrix, s):
    # 判断图是否为空，如果为空直接退出
    INF = 1 << 9
    if matrix is None:
        return None
    dist = [INF] * len(matrix)
    dist[s] = 0
    Q = [i for i in range(len(matrix))]
    # dist_init在dist完成后基本可以说是其副本
    dist_init = [i for i in matrix[s]]
    while Q:
        # 判断除Q中已去除点外最小元素值
        u_dist = min([d for v, d in enumerate(dist_init) if v in Q])
        # 上述元素值的索引值
        u = dist_init.index(u_dist)
        Q.remove(u)
        for v, d in enumerate(matrix[u]):
            if 0 < d < INF:
                # 判断如果从起点绕u点距离比由起点沿其它路径到目标点更近，则替换
                # 因为起始值肯定是由0开始（权值暂只考虑大于0）
                # 所以第一轮会把dist替换成dist_init一样的列表
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    dist_init[v] = dist[v]
    # 结果代表顶点到每一个结点最小距离
    return dist


if __name__ == '__main__':
    lis = [('V0', 'V1', 1), ('V0', 'V2', 5), ('V1', 'V2', 3), ('V1', 'V3', 7),
           ('V1', 'V4', 5), ('V2', 'V4', 1), ('V2', 'V5', 7), ('V3', 'V4', 2),
           ('V3', 'V6', 3), ('V4', 'V5', 3), ('V4', 'V6', 6), ('V4', 'V7', 9),
           ('V5', 'V7', 5), ('V6', 'V7', 2), ('V6', 'V8', 7), ('V7', 'V8', 4)]
    dic = {}
    for j in graph_with_weight(lis)[0]:
        dic[graph_with_weight(lis)[0].index(j)] = j
    matrix = graph_with_weight(lis)[1]
    print(dic)
    print('~' * 40)
    print(matrix)
    print('~' * 40)
    print(dijkstra(matrix, 0))