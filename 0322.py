from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        # 类似爬楼梯
        for i in range(1, n + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
        return dp[n] if dp[n] != float("inf") else -1
