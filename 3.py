#!/usr/bin/env python3
# coding:utf-8

"""
1.找出数组中重复的数字
在一个长度为n的数组里的所有数字都在0-n-1的范围内，数组中某些数字是重复的，请找出数组中任意一个重复的数字
2.不修改数组找出重复的数字
在一个长度为n+1的数组里的所有数字都在1-n的范围内，所以数组中至少有一个数字是重复的，请找出数组中任意一个重复数字，但不能修改
输入的数组。
"""


class Solution(object):

    def find_dup_number(self, data):
        if not data:
            return

        length = len(data)
        if any(map(lambda x: x > length - 1 or x < 0, data)):
            return

        for i in range(length):
            while data[i] != i:
                print(data[i], data[data[i]])
                if data[i] == data[data[i]]:
                    return data[i]

                tmp = data[i]
                data[i], data[tmp] = data[tmp], data[i]
        return

    def find_dup_number_v2(self, data):
        if not data:
            return

        length = len(data)
        if any(map(lambda x: x > length or x < 1, data)):
            return

        start = 1
        end = length - 1

        while end >= start:
            middle = ((end-start) >> 1) + start

            count = self.count_range(data, start, middle)

            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > (middle-start+1):
                end = middle
            else:
                start = middle + 1

    def count_range(self, data, start, end):
        count = 0

        for item in data:
            if item >= start and item <= end:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    # data1 = [4, 0, 1, 4, 2, 5, 3]
    # result = solution.find_dup_number(data1)
    # print(result)
    data2 = [1, 2, 3, 4, 5, 6, 5]
    result = solution.find_dup_number_v2(data2)
    print(result)

