#!/usr/bin/env python3
# coding:utf-8

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树，
假设输入的前序和中序遍历的结果中都不含重复的数字。
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution(object):

    def rebuild_binary_tree(self, pre, mid):
        if not pre or not mid:
            return None

        node = Node(pre[0])
        node_index = mid.index(node.data) + 1

        node.left = self.rebuild_binary_tree(pre[1:node_index], mid[:node_index+1])
        node.right = self.rebuild_binary_tree(pre[node_index:], mid[node_index:])

        return node

    def after_order(self, root):
        if not root:
            return

        self.after_order(root.left)
        self.after_order(root.right)
        print(root.data)


if __name__ == '__main__':
    pre = [10, 5, 1, 7, 12, 9, 15]
    mid = [1, 5, 7, 10, 9, 12, 15]

    solution = Solution()
    root = solution.rebuild_binary_tree(pre, mid)
    solution.after_order(root)
