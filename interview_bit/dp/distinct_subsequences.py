# nodemon --watch distinct_subsequences.py -e py --exec "mypy distinct_subsequences.py && python distinct_subsequences.py"

from pprint import pprint


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        len_A = len(A)
        len_B = len(B)
        dp = [[0 for _ in range(len_B + 1)] for _ in range(len_A + 1)]
        for i in range(len_A + 1):
            dp[i][0] = 1
        for i in range(1, len_A+1):
            for j in range(1, len_B + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        pprint(dp)
        return dp[len_A][len_B]


def test1():
    A = "rabbbit"
    B = "rabbit"
    sol = Solution()
    print(sol.numDistinct(A, B))


test1()
