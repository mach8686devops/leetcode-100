class Solution:
    def solve(self, triangle):
        m = len(triangle)
        dp = [0] * (len(triangle[m - 1]) + 1)
        for i in range(m - 1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
