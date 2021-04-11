class Solution(object):
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        n = len(coins)
        for j in range(n):
            for i in range(1, amount + 1):
                if i >= coins[j]:
                    dp[i] += dp[i - coins[j]]
        return dp[-1]


amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))
