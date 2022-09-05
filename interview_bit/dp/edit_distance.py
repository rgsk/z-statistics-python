# nodemon --watch edit_distance.py -e py --exec "mypy edit_distance.py && python edit_distance.py"

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        len_A = len(A)
        len_B = len(B)
        dp = [[0 for j in range(len_B + 1)] for i in range(len_A + 1)]
        for i in range(len_A+1):
            for j in range(len_B+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
        for i in range(1, len_A+1):
            for j in range(1, len_B+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
        return dp[len_A][len_B]


sol = Solution()


def test1():
    A = 'abad'
    B = 'abac'
    print(sol.minDistance(A, B))


def test2():
    A = 'Anshuman'
    B = 'Antihuman'
    print(sol.minDistance(A, B))


test2()
