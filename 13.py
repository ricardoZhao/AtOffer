#!/usr/bin/env python
# coding=utf-8


"""
地上有一个m行n列的方格。一个机器人从坐标(0,0)的格子开始
移动，它每次可以向左，右，上，下移动一格，但不能进入行坐标
和列坐标的数位之和大于k的格子。例如:当k为18时，机器人能够进入
方格(35,37),因为3+5+3+7=18,但它不能进入方格(35, 38),因为
3+5+3+8=19,请问该机器人能够到达多少个格子.
"""


class Solution(object):

    def move_count(self, k, rows, cols):
        if rows <= 0 or cols <= 0:
            return 0

        visited = [False] * rows * cols

        count = self.get_move_count(k, rows, cols, 0, 0, visited)
        return count

    def get_move_count(self, k, rows, cols, row, col, visited):
        count = 0

        index = row * cols + col
        if row < 0 or col < 0 or row >= rows or col >= cols or visited[index] or self.get_digit_sum(row) + self.get_digit_sum(col) > k:
            return count

        visited[index] = True
        count = 1 + self.get_move_count(k, rows, cols, row, col-1, visited) + \
                self.get_move_count(k, rows, cols, row, col+1, visited) + \
                self.get_move_count(k, rows, cols, row+1, col, visited) + \
                self.get_move_count(k, rows, cols, row-1, col, visited)
        print(row, col, count)
        return count

    def get_digit_sum(self, number):
        sum_number = 0
        while number > 0:
            sum_number += number % 10
            number //= 10
        return sum_number


if __name__ == '__main__':
    solution = Solution()
    count = solution.move_count(4, 6, 6)
    print(count)
