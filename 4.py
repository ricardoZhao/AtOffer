#!/usr/bin/env python3
# coding:utf-8

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序， 请完成一个函数，输入这样的
一个二维数组和一个整数，判断数组中是否含有该整数.
"""


class Solution(object):

    def find_number(self, data, rows, columns, number):
        if not data:
            return False

        if len(data) != rows and any(map(lambda x: len(x) != columns, data)):
            return False

        row = 0
        column = columns - 1

        while row <= rows and column >= 0:
            if data[row][column] == number:
                return (row, column)
            elif data[row][column] > number:
                column -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    solution = Solution()

    data = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [7, 8, 9, 10]
    ]
    result = solution.find_number(data, 4, 4, 9)
    print(result)
