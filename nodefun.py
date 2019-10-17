#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by CK 2019-04-11 04:43:20


class Node:
    def __init__(self, value=None, left=None, right=None,
                 father=None, level=None):
        self.value = value
        self.left = left
        self.right = right
        self.father = father
        self.level = level

    def __str__(self):
        return str(self.value)


class Tree:

    lis = []
    route = []
    route_begin = []
    n_t_l = []
    count = 0

    def __init__(self):
        self.root = None
        self.lt = []

    def add(self, number):
        node = Node(number)
        if self.root is None:
            self.root = node
            self.lt.append(self.root)
            self.root.father = None
            self.root.level = 0
        else:
            while True:
                point = self.lt[0]
                if not point.left:
                    point.left = node
                    self.lt.append(point.left)
                    point.left.father = point
                    point.left.level = point.level + 1
                    return
                elif not point.right:
                    point.right = node
                    self.lt.append(point.right)
                    point.right.father = point
                    point.right.level = point.level + 1
                    self.lt.pop(0)
                    return

    def num_to_list(self, root):
        if str(root) != 'None':
            self.count += int(str(root))
        self.n_t_l.append(self.count)
        if root.father:
            self.num_to_list(root.father)
        else:
            self.count = 0

    def get_left_leaves(self, root):
        if root is None:
            return
        #  self.get_left_leaves(root.left)
        #  lis.append(str(root.left))
        #  return lis
        if root.left and str(root.left) != 'None':
            self.lis.append(root.left)
            #  print(root.left, 'this is root.left')
        self.get_left_leaves(root.left)
        self.get_left_leaves(root.right)

    def traverse_by_layer(self, root):
        if not root:
            return
        # print(root)
        start = [root]
        temp = []
        result = [root]
        while start:
            for i in start:
                if i.left:
                    temp.append(i.left)
                    result.append(i.left)
                    # print(i.left)
                if i.right:
                    temp.append(i.right)
                    result.append(i.right)
                    # print(i.right)
            start = temp
            temp = []
        return result

    def get_father_value(self, child):
        if str(child) == 'None':
            return
        else:
            self.route.append(str(child))
        if child.father:
            self.get_father_value(child.father)

    def traverse_from_end(self, root):
        if not root:
            return
        self.traverse_from_end(root.left)
        self.traverse_from_end(root.right)
        if not root.left and not root.right:
            self.route_begin.append(root)

    def tree_structure(self, root):
        if not root:
            return
        print('|    ' * root.level, '+--', root)
        self.tree_structure(root.left)
        self.tree_structure(root.right)


if __name__ == '__main__':
    t = Tree()
    a = [6, 2, 1, 5, 7, 9, 0, 3, 4, None, 8]
    for i in a:
        t.add(i)
    c = t.traverse_by_layer(t.root.left)
    d = t.traverse_by_layer(t.root.right)
    e = max(x.level for x in c) + max(y.level for y in d)
    print(e)
    t.tree_structure(t.root)