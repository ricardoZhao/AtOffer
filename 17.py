#!/usr/bin/env python
# coding=utf-8

"""
输入数字n，按顺序打印出从1到最大的n位十进制数，比如输入3,
则打印出1，2，3一直到最大的3位数999
"""

class Solution(object):

    def print_1_to_max_n_digits(self, n):

        if (n <= 0):
            return

        number = ['0'] * n

        for i in range(0, 10):
            number[0] = str(i)
            self.print_to_max_n_recurisive(number, n, 0)

    def print_to_max_n_recurisive(self, number, n, index):
        if index == n - 1:
            self.print_number(number)
            return

        for i in range(0, 10):
            number[index+1] = str(i)
            self.print_to_max_n_recurisive(number, n, index+1)

    def print_number(self, number):
        start_index = -1
        for index, elem in enumerate(number):
            if elem != '0':
                start_index = index
                break
        print(''.join(number[start_index:]))


if __name__ == '__main__':
    solution = Solution()
    solution.print_1_to_max_n_digits(4)
