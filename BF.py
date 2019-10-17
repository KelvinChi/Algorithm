#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def brute_force(s1, s2):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1
            j = 0
    if i == len(s1):
        return False
    return True



s1 = 'whatisthefuck'
s2 = 'hefq'
print(brute_force(s1, s2))


