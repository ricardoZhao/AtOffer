#!/usr/bin/env python
# coding=utf-8

"""
请实现一个函数，输入一个整数，输出该数二进制表示中
1的个数，例如，把9表示成二进制是1001，有2位是1。因此
如果输入9，则该函数输出2
"""


class Solution(object):

    def number_of_one(self, n):
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution()
    result = solution.number_of_one(-9)
    print(result)
