#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
约瑟夫问题：
    著名犹太历史学家Josephus有过以下故事：在罗马人占领乔塔帕特后，39个犹太人与Josephus
    及他的朋友躲到一个洞中，39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，
    41个人排成一个圆圈，由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新
    报数，直到所有人都自杀身亡。
'''

# 建立列表，起始为1
def circul_list(num):
    lis = []
    for i in range(num):
        lis.append(i + 1)
    return lis


def people_list(lis):
    pin = 1
    result = []
    # 判定假如列表里只有2人（有一个None值存在）后，停止循环
    while len(set(lis)) != 3:
        for i in range(len(lis)):
            # 每3个死亡一人
            if pin == 3 and lis[i]:
                result.append(lis[i])
                lis[i] = None
                pin = 1
            if lis[i]:
                pin += 1
    # 注意result后两个数表示幸存者数字
    for i in set(lis):
        if i:
            result.append(i)
    return result


lis = people_list(circul_list(41))
print('自杀顺序：%s。' %lis[:-2], '幸存者：%s。' % lis[-2:], sep=' \n')