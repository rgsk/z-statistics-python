# nodemon --watch longest_repeating_subsequence.py -e py --exec "mypy longest_repeating_subsequence.py && python longest_repeating_subsequence.py"

class Solution:
    # @param A : string
    # @return an integer

    def anytwo(self, A):
        n = len(A)
        dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and A[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n][n]


def test1():
    A = "aabb"
    sol = Solution()
    print(sol.anytwo(A))


test1()


def test2():
    A = "aabebcdd"
    sol = Solution()
    print(sol.anytwo(A))


test2()
