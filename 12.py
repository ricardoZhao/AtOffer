#!/usr/bin/env python
# coding=utf-8


"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串
所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以向
左，右，上，下移动一格。如果一条路径经过了矩阵的某一格，那么 
该路径不能再次进入该格子。

a b t g
c f c s 
j d e h

a->b->f->d
"""


class Solution(object):

    def has_path(self, matrix, rows, cols, path):
        if not matrix:
            return False

        visited = [False] * rows * cols

        for row in range(rows):
            for col in range(cols):
                if self.find_path(matrix, rows, cols, path, row, col, visited):
                    return True

        return False

    def find_path(self, matrix, rows, cols, path, row, col, visited):
        if not path:
            return True

        index = row * cols + col

        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[index] != path[0] or visited[index]:
            return False

        visited[index] = True

        if (self.find_path(matrix, rows, cols, path[1:], row, col+1, visited) or 
            self.find_path(matrix, rows, cols, path[1:], row, col-1, visited) or 
            self.find_path(matrix, rows, cols, path[1:], row+1, col, visited) or 
            self.find_path(matrix, rows, cols, path[1:], row-1, col, visited)):
            return True

        visited[index] = False   
        return False


    """
    def has_path(self, matrix, rows, cols, path):
        if not matrix:
            return False

        for i in range(rows):
            for j in range(cols):
                if matrix[i*cols+j] == path[0]:
                    if self.find_path(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find_path(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i*cols+j] = 0

        if j+1 < cols and matrix[i*cols+j+1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j+1)
        elif j-1 >= 0 and matrix[i*cols+j-1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j-1)
        elif i+1 < rows and matrix[(i+1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i+1, j)
        elif i-1 >= 0 and matrix[(i-1)*cols+j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i-1, j)
        return False
    """


if __name__ == '__main__':
    solution = Solution()
    matrix = 'abtgcfcsjdeh'
    result = solution.has_path(matrix, 3, 4, 'tgsh')
    print(result)
