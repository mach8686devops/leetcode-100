class Solution:
    """
    @param n: the number of people
    @param m: the number of groups
    @return: the number of grouping options
    """

    def groupingOptions(self, n, m):
        # write your code here
        if m > n:
            return 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 1
        for i in range(2, n + 1, 1):
            for j in range(1, i, 1):
                for k in range(1, j + 1, 1):
                    dp[i][j] = dp[i][j] + dp[i - j][k]
        return dp[n][m]
