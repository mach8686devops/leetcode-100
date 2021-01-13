# 股票问题全集


# 买卖股票的最佳时机


class Solution:
    def maxProfit(self, prices):
        ans = 0
        for day in range(len(prices) - 1):
            diff = prices[day + 1] - prices[day]
            if diff > 0:
                ans += diff
        return ans


print(Solution().maxProfit(prices=[5, 7, 3, 9]))
