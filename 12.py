#!/usr/bin/env python
# coding=utf-8

"""
输入一个整数n,求从１到n这n个整数的10进制表示中１出现的次数。
"""


class Solution(object):

    def count_digit_one(self, n):
        num = 0
        base = 1

        while n // base != 0:
            cur = n // base % 10
            right = n % base
            left = n // (base * 10)

            if cur == 0:
                num += left * base
            elif cur == 1:
                num += left * base + right + 1
            else:
                num += (left + 1) * base

            base *= 10
        return num


if __name__ == '__main__':
    solution = Solution()
    n = 31256
    num = solution.count_digit_one(n)
    print(num)
