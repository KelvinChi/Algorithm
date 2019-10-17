#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


def infix_to_rpn(formula):
    temp = ''
    symbolic = []
    result = []
    for i in formula:
        if i == ' ':
            continue
        elif i.isdigit():
            temp += i
            continue
        if temp:
            result.append(temp)
            try:
                if symbolic[-1] == '*' or symbolic[-1] == '/':
                    result.append(symbolic.pop())
                elif i == ')':
                    judge(result, symbolic)
            except IndexError:
                pass
            temp = ''
        symbolic.append(i)
    if temp:
        result.append(temp)
    judge(result, symbolic)
    return result


def judge(result, symbolic):
    try:
        while symbolic[-1] != '(' or len(symbolic) != 0:
            if symbolic[-1] != ')' and symbolic[-1] != '(':
                result.append(symbolic.pop())
            else:
                symbolic.pop()
    except IndexError:
        pass


a = '(12 + 4) * 5 + 43 / 12 + 2 * (5 + 12 + 123)'
# a = '(12 + 4) * 5'
b = '12, 4, +, 5, *, 43, 12, /, 2, 5, 12, 123, +, +, *, +, +'
print(infix_to_rpn(a))