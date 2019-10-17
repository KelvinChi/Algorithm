#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import numpy as np


# 假设每个节点的值不相同且都以字母表示，且为连通图
def graph(lis):
    string = []
    for i in lis:
        string.extend([i[0], i[1]])
    # 下边是简单粗暴的处理方法，也可以通过遍历、判断元素是否在新组成的列表中，没有深入想过哪种效率更高
    string = sorted(set(string))
    matrix = np.zeros((len(string), len(string)))
    # 遍历输入的列表，读取元组数据，string中的数据索引值跟新建的matrix中的有对应关系，以建立邻接矩阵
    for j in lis:
        # 无向图的matrix[i][j] = matrix[j][i]，而有向图要区别
        matrix[string.index(j[0])][string.index(
            j[1])] = matrix[string.index(j[1])][string.index(j[0])] = 1
    return string, matrix


# 以下只考虑无向图
def dfs(matrix, row=0, col=0):
    # 邻接矩阵都为方形矩阵
    global col_list, dic
    # 用col标识已走过的路
    while col < len(matrix):
        if col not in col_list and matrix[row][col] == 1:
            print('%s --> %s' % (dic[row], dic[col]))
            col_list.append(col)
            row = col
            dfs(matrix, row, col)
        col += 1
    # 下码表示如果当前无路便退回到上一级
    if col == len(matrix):
        row -= 1
        col -= 1
        return 0 if row == 0 else dfs(matrix, row, col)


# 同样只考虑无向图
def bfs(matrix):
    global used_vertex, unused_vertex
    for i in range(len(matrix[0])):
        if matrix[unused_vertex[0]][i] == 1:
            # 判断列代表的元素是否已经查过，未查过才放到unused_vertex表中
            if (i not in used_vertex) and (i not in unused_vertex):
                unused_vertex.append(i)
    used_vertex.append(unused_vertex.pop(0))
    if unused_vertex:
        bfs(matrix)


if __name__ == '__main__':
    lis = [('A', 'B'), ('A', 'F'), ('B', 'C'), ('B', 'G'), ('B', 'I'),
           ('C', 'I'), ('C', 'D'), ('D', 'E'), ('D', 'G'), ('D', 'H'),
           ('E', 'F'), ('F', 'G'), ('G', 'H'), ('D', 'I'), ('E', 'H')]
    for i in graph(lis):
        print(i)
    matrix = graph(lis)[1]
    # 深度优先遍历
    col_list = []
    dic = {}
    for j in graph(lis)[0]:
        dic[graph(lis)[0].index(j)] = j
    dfs(matrix)
    # 广度优先遍历
    used_vertex = []
    unused_vertex = [0]
    bfs(matrix)
    print(used_vertex)
