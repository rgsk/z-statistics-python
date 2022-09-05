# nodemon --watch merge_elements.py -e py --exec "mypy merge_elements.py && python merge_elements.py"

from pprint import pprint
from sys import prefix


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pf = PrefixSums(A)
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        diff = 1
        while diff <= n-1:
            for i in range(0, n - diff):
                j = i + diff
                dp[i][j] = 1000
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], pf.get_sum(
                        i, k) + dp[i][k] + pf.get_sum(k+1, j) + dp[k+1][j])
            diff += 1
        return dp[0][n-1]


class PrefixSums:
    def __init__(self, arr) -> None:
        n = len(arr)
        self.prefix_sums = [0 for _ in range(n+1)]
        for i in range(n):
            self.prefix_sums[i+1] = self.prefix_sums[i] + arr[i]

    def get_sum(self, i, j):
        return self.prefix_sums[j+1] - self.prefix_sums[i]


def test():
    arr = [1, 2, 3, 4]
    sol = Solution()
    print(sol.solve(arr))


test()
value = '0 46 46 0 2 47 1 24 45 0 0 24 18 29 27 11 0 0 40 12 4 0 0 0 49 42 13 5 12 45 10 0 29 11 22 15 17 41 34 23 11 35 0 18 47 0 38 37 3 37 0 43 50 0 25 12 0 38 28 37 5 4 12 23 31 9 26 19 11 21 0 0 40 18 44 0 0 0 0 30 26 37 0 26 39 10 1 0 0 3 50 46 1 38 38 7 6 38 27 7 25 30 0 0 36 37 6 39 40 32 41 12 3 44 44 39 2 26 40 36 35 21 14 41 48 50 21 0 0 23 49 21 11 27 40 47 49'
print(len(value.split(' ')))
print('{k}'.format(1))
