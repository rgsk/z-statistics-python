# nodemon --watch chain_of_pairs.py -e py --exec "mypy chain_of_pairs.py && python chain_of_pairs.py"

class Solution:
    def solve(self, A):
        n = len(A)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if A[i][0] > A[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def helper(self, A, index, last_b, memo):
        if index == len(A):
            return 0
        if memo[index][last_b] != -1:
            return memo[index][last_b]
        if A[index][0] > last_b:
            memo[index][last_b] = max(
                1 + self.helper(A, index + 1, A[index][1], memo), self.helper(A, index+1, last_b, memo))
        else:
            memo[index][last_b] = self.helper(A, index+1, last_b, memo)
        return memo[index][last_b]

    def solve_memo(self, A):
        rows = len(A)
        cols = max([v[1] for v in A]) + 1
        memo = [[-1 for _ in range(cols)] for _ in range(rows)]
        return self.helper(A, 0, 0, memo)


def test1():
    A = [[5, 24],
         [39, 60],
         [15, 28],
         [27, 40],
         [50, 90]
         ]
    sol = Solution()
    print(sol.solve_memo(A))


test1()


def test2():
    A = [[10, 20],
         [1, 2]
         ]
    sol = Solution()
    print(sol.solve_memo(A))


test2()
