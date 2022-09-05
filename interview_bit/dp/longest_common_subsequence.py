# nodemon --watch longest_common_subsequence.py -e py --exec "mypy longest_common_subsequence.py && python longest_common_subsequence.py"


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def solve(self, A: str, B: str):
        total_rows = len(A)
        total_columns = len(B)
        dp = [[0 for i in range(total_columns + 1)]
              for i in range(total_rows + 1)]
        for i in range(1, total_rows + 1):
            for j in range(1, total_columns + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[total_rows][total_columns]


sol = Solution()
A = "abbcdgf"
B = "bbadcgf"
print(sol.solve(A, B))
