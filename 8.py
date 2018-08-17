#!/usr/bin/env python3
# coding:utf8

"""
给定一棵二叉树和其中一个节点，如何找出中序遍历序列的下一个节点?
树中的节点除了有两个分别指向左，右子节点的指针，还有一个指向父节点
的指针
"""


class Node:

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class Solution(object):

    def get_next(self, node):
        if not node:
            return None

        next_node = None
        if node.right:
            right = node.right
            while right.left:
                right = right.left
            next_node = right
        elif node.parent:
            cur = node
            parent = node.parent

            while parent and cur == parent.right:
                cur = parent
                parent = parent.parent

            next_node = parent
        return next_node


if __name__ == '__main__':
    solution = Solution()

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    a.left = b
    a.right = c
    b.left = d
    d.parent = b
    b.right = e
    b.parent = a
    e.left = h
    e.right = i
    e.parent = b
    h.parent = e
    i.parent = e

    c.left = f
    c.right = g
    c.parent = a
    f.parent = c
    g.parent = c

    next_node = solution.get_next(i)
    print(next_node.data)
