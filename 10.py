#!/usr/bin/env python3
# coding:utf-8

"""
求斐波那契数列的第n项
"""


class Solution(object):

    def fab1(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        ret = self.fab1(n-1) + self.fab1(n-2)
        return ret

    def fab2(self, n):
        """
        采用递归会有很多数值的重复计算，效率不如循环
        """
        if n <= 1:
            return n
        fab_one = 1
        fab_two = 0
        fab_n = 0

        for i in range(2, n+1):
            fab_n = fab_one + fab_two
            fab_two = fab_one
            fab_one = fab_n

        return fab_n


if __name__ == '__main__':
    solution = Solution()

    print(solution.fab1(5))
    print(solution.fab2(5))
