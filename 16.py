#!/usr/bin/env python
# coding=utf-8

"""
实现函数def power(base, exp), 求base的exp次方，
不得使用库函数，同时不需要考虑大数问题
"""


class Solution(object):

    def power(self, base, exp):
        if exp == 0:
            return 1
        if exp == 1:
            return base

        result = self.power(base, exp>>1)

        result *= result

        if exp & 0x1 == 1:
            result *= base

        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.power(2, 3)
    print(result)
