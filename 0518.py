class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for j in range(len(coins)):
            for i in range(1, amount + 1):
                if i >= coins[j]:
                    dp[i] += dp[i - coins[j]]
        return dp[-1]
