#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def next_fun(string):
    string = str(len(string)) + string
    i = 0 # 前缀
    j = 1 # 后缀
    next_lis = [0] * len(string)
    while j < int(string[0]):
        if i == 0 or string[j] == string[i]:
            i += 1
            j += 1
            # 判断如果字符有一段重复，则next表也没必要增加
            if string[j] != string[i]:
                next_lis[j] = i
            else:
                next_lis[j] = next_lis[i]
        else:
            i = next_lis[i]
    return next_lis


def kmp(s1, s2):
    i = j = 0
    next_lis = next_fun(s2)
    while i < len(s1) and j < len(s2):
        # 如果当前字符相同，则同时向后移动一位再对比
        if s1[i] == s2[j]:
            i += 1
            j += 1
        # 如果当前字符不同，则按照next_lis的规则来移动等匹配字符的位置
        else:
            i += 1
            j = next_lis[j + 1]
    # 字符串如果匹配完成，那么j一定与匹配的字符串等长
    if j != len(s2):
        return False
    return True


s1 = 'whatisthefuck'
s2 = 'isthe'
print(next_fun(s2))
print(kmp(s1, s2))