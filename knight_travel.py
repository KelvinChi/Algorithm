#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import numpy


def knight_travel():
    global footprint
    while step < 65:
        judge = next_step()
        # 判断如果当前没有可用位置，则退回上一位置
        if judge:
            footprint.pop()
            next_step()


def next_step():
    global step, matrix, footprint
    row = footprint[-1][0]
    col = footprint[-1][1]
    if row - 2 >= 0 and col + 1 < 8 and matrix[row - 2][col + 1] == 0:
        row -= 2
        col += 1
    elif row - 1 >= 0 and col + 2 < 8 and matrix[row - 1][col + 2] == 0:
        row -= 1
        col += 2
    elif row + 1 < 8 and col + 2 < 8 and matrix[row + 1][col + 2] == 0:
        row += 1
        col += 2
    elif row + 2 < 8 and col + 1 < 8 and matrix[row + 2][col + 1] == 0:
        row += 2
        col += 1
    elif row + 2 < 8 and col - 1 >= 0 and matrix[row + 2][col - 1] == 0:
        row += 2
        col -= 1
    elif row + 1 < 8 and col - 2 >= 0 and matrix[row + 1][col - 2] == 0:
        row += 1
        col -= 2
    elif row - 1 >= 0 and col - 2 >= 0 and matrix[row - 1][col - 2] == 0:
        row -= 1
        col -= 2
    elif row - 2 >= 0 and col - 1 >= 0 and matrix[row - 2][col - 1] == 0:
        row -= 2
        col -= 1
    else:
        return True
    matrix[row][col] = step
    footprint.append([row, col])
    step += 1


if __name__ == '__main__':
    step = 2
    # 以列表形式存储每个步点位置，方便回溯
    footprint = [[4, 3]]
    matrix = numpy.zeros((8, 8))
    matrix[4][3] = 1
    knight_travel()
    print(matrix)
