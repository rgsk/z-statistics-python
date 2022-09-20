# nodemon --watch 785_Range_Query_on_a_List.py -e py --exec "mypy 785_Range_Query_on_a_List.py && python 785_Range_Query_on_a_List.py"
class RangeSum:
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0] + [v for v in nums]
        for i in range(1, len(nums)+1):
            self.prefix[i] += self.prefix[i-1]

    def total(self, i, j):
        return self.prefix[j] - self.prefix[i]


def test1():
    #      0, 1, 2, 3, 4, 5
    arr = [1, 2, 5, 0, 3, 7]
    rs = RangeSum(arr)
    print(rs.total(0, 6))


test1()
