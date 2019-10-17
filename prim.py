#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import numpy as np


# 建立邻接矩阵
def graph_with_weight(lis):
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
            j[1])] = matrix[string.index(j[1])][string.index(j[0])] = j[2]
    # 除对角线向所有为0的格填充为inf
    for x in range(len(string)):
        for y in range(len(string)):
            if x != y and matrix[x][y] == 0:
                matrix[x][y] = 1 << 9  # 此处需要注意数据大小，不能让图内数据大小超过这个
    return string, matrix

# 下边是我自己写的，烂啊
# def prim(matrix):
#     # 默认以0开始，实际使用时可修改
#     vertexes = [0]
#     edges = []
#     values = []
#     while len(vertexes) != len(matrix):
#         min_temp = None
#         # 已知顶点，添加所有与之相关且未被添加过的边入edges
#         row = vertexes[-1]
#         # 先添加以顶点为起点的边
#         for col in range(len(matrix)):
#             if col > row and matrix[row][col] != 1 << 10 and [row, col, matrix[row][col]] not in edges:
#                 edges.append([row, col, matrix[row][col]])
#         # 添加以顶点为终点的边
#         col = row
#         for row in range(len(matrix)):
#             if col > row and matrix[row][col] != 1 << 10 and [row, col, matrix[row][col]] not in edges:
#                 edges.append([row, col, matrix[row][col]])
#         # 如果row与col都在已添加顶点的表中，表示有环存在，应该去掉
#         for i in range(len(edges)):
#             if edges[i][0] in vertexes and edges[i][1] in vertexes:
#                 edges[i] = None
#         temp = []
#         for j in edges:
#             if j and j not in temp:
#                 temp.append(j)
#         edges = temp
#         for i in edges:
#             # 得到当前最小值
#             if min_temp is None:
#                 min_temp = i
#             else:
#                 if min_temp[2] > i[2]:
#                     min_temp = i
#         for j in range(2):
#             if min_temp[j] not in vertexes:
#                 vertexes.append(min_temp[j])
#         values.append(min_temp[2])
#     return vertexes, values

# 用图画比较好理解，就是建立一行，每次将它与寻找到的最小点代表的下一行对比，如果元素已经被访问
# 则不变，反之取两行间的最小值再构迭代成新行，然后继续重复对比，得到的每一次最小代的index就是
# 结点被访问的顺序，画图就很好理解了


def prim(matrix, vertex_num):
    INF = 1 << 10
    visit = [False] * vertex_num
    dist = [INF] * vertex_num
    preIndex = [0] * vertex_num

    for i in range(vertex_num):

        minDist = INF + 1
        nextIndex = -1

        for j in range(vertex_num):
            if dist[j] < minDist and not visit[j]:
                minDist = dist[j]
                nextIndex = j

        print(nextIndex)
        visit[nextIndex] = True

        for j in range(vertex_num):
            if dist[j] > matrix[nextIndex][j] and not visit[j]:
                dist[j] = matrix[nextIndex][j]
                preIndex[j] = nextIndex
    return dist, preIndex


if __name__ == '__main__':
    lis = [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9),
           ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6),
           ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)]
    dic = {}
    for j in graph_with_weight(lis)[0]:
        dic[graph_with_weight(lis)[0].index(j)] = j
    matrix = graph_with_weight(lis)[1]

    print(matrix)

    print(prim(matrix, 7))
