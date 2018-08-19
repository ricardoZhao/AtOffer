#!/usr/bin/env python
# coding=utf-8


"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为
数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转
数组的最小元素。例如，数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，
该数组的最小值为1.
"""


class Solution(object):

    def min(self, data):
        if not data:
            return

        length = len(data)

        index_mid = index1 = 0
        index2 = length - 1

        while data[index1] >= data[index2]:
            if index2 - index1 == 1:
                index_mid = index2
                break

            index_mid = (index1 + index2) / 2

            # 如果三者相同，没法判断中间的数字是位于前面的子数组还是后面的子数组
            if data[index1] == data[index2] == data[index_mid]:
                return self.min_in_data(data, index1, index2)

            if data[index_mid] >= data[index1]:
                index1 = index_mid

            elif data[index_mid] <= data[index2]:
                index2 = index_mid

        return data[index_mid]

    def min_in_data(self, data, index1, index2):
        result = data[index1]

        for i in range(index1+1, index2+1):
            if result > data[i]:
                result = data[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    # data = [3, 4, 5, 1, 2]
    # min_number = solution.min(data)
    data = [1, 0, 1, 1, 1]
    min_number = solution.min(data)
    print(min_number)
