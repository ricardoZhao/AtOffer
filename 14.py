#!/usr/bin/env python
# coding=utf-8

"""
给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
每段绳子的长度记为k[0],k[1],…,k[m].请问k[0]k[1]…*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
"""


class Solution(object):

    def max_after_cutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        li = [0, 1, 2, 3]

        for i in range(4, length+1):
            max_val = 0

            for j in range(1, i//2+1):
                temp = li[j] * li[i-j]

                if temp > max_val:
                    max_val = temp
            li.append(max_val)

        return li[-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.max_after_cutting(8)
    print(result)
