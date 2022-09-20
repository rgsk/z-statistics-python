# nodemon --watch 786_Range_Query_on_Two_Dimensional_List.py -e py --exec "mypy 786_Range_Query_on_Two_Dimensional_List.py && python 786_Range_Query_on_Two_Dimensional_List.py"

from pprint import pprint
import numpy as np


class RangeSum:
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0] + [v for v in nums]
        for i in range(1, len(nums)+1):
            self.prefix[i] += self.prefix[i-1]

    def total(self, i, j):
        return self.prefix[j] - self.prefix[i]


class RangeSumMatrix1:
    def __init__(self, matrix):
        self.prefix_matrix = [RangeSum(row) for row in matrix]

    def total(self, row0, col0, row1, col1):
        s = 0
        for i in range(row0, row1 + 1):
            s += self.prefix_matrix[i].total(col0, col1 + 1)
        return s


class RangeSumMatrix:
    def __init__(self, matrix):
        self.pf = self.getPrefix(matrix)
        for row in self.pf:
            print(row)

    def total(self, row0, col0, row1, col1):
        ret = 0
        ret += self.pf[row1][col1]
        row_in_range = row0 > 0
        col_in_range = col0 > 0
        if row_in_range:
            ret -= self.pf[row0 - 1][col1]
        if col_in_range:
            ret -= self.pf[row1][col0 - 1]
        if row_in_range and col_in_range:
            ret += self.pf[row0 - 1][col0 - 1]
        return ret

    def getPrefix(self, matrix):
        if not matrix:
            return matrix

        R, C = len(matrix), len(matrix[0])
        for r in range(1, R):
            for c in range(C):
                matrix[r][c] += matrix[r - 1][c]

        for r in range(R):
            for c in range(1, C):
                matrix[r][c] += matrix[r][c - 1]

        return matrix


def test1():
    matrix = [[1, 2, 3], [4, 5, 6]]
    v = np.array(matrix)
    print(v)
    rsm = RangeSumMatrix(matrix)
    print(rsm.total(0, 0, 1, 1))
    print(rsm.total(0, 1, 0, 2))


test1()

def binary_search_get_bigger_index(arr, v, start_index = 0):
    i = start_index
    n = len(arr)
    incr = n//2
    while incr > 0 and i < n:
        while i + incr >= n or arr[i + incr] > v:
            incr //= 2
        i += incr
    return i + 1

print(binary_search_get_bigger_index([3, 3, 3, 3, 4, 4, 8], 8))
        