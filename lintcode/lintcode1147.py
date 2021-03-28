class Solution:
    """
    @param low: the simple task
    @param high: the complex task
    @return: the most value
    """

    def workPlan(self, low, high):
        # Write your code here.
        m = len(low)
        n = len(high)
        dp = [0 for _ in range(10500)]
        dp[1] = low[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1] + low[i - 1], dp[i - 2] + high[i - 1])
        return dp[n]
