# 股票问题全集
from typing import List


# 买卖股票的最佳时机


class Solution121:
    def maxProfit(self, prices):
        ans = 0
        for day in range(len(prices) - 1):
            diff = prices[day + 1] - prices[day]
            if diff > 0:
                ans += diff
        return ans


print(Solution121().maxProfit(prices=[5, 7, 3, 9]))


class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit


class Solution123:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell1, sell2, buy1, buy2 = 0, 0, -float('inf'), -float('inf')
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


class Solution188:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)
        # if 2*k >= n  意味着交易不受限制，参考上上题
        if 2 * k >= n:
            res = 0
            for i in range(1, n):
                res += max(prices[i] - prices[i - 1], 0)
            return res

        # dp 数组定义及初始化
        dp = [[-prices[0], 0] for _ in range(k)]  # [buy_1 sell_1] [buy_2 sell_2] ==> [buy_k sell_k] (k times)

        for i in range(1, n):
            for j in range(1, k + 1):
                if j == 1:
                    last_sell = 0
                else:
                    last_sell = dp[j - 2][1]
                # for all buys
                dp[j - 1][0] = max(last_sell - prices[i], dp[j - 1][0])
                # for all sells
                dp[j - 1][1] = max(dp[j - 1][0] + prices[i], dp[j - 1][1])

        return dp[-1][1]


class Solution309:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_buy, dp_sell = -prices[0], 0
        dp_pre_sell = 0
        for i in range(1, n):
            dp_buy = max(dp_pre_sell - prices[i], dp_buy)
            dp_pre_sell = dp_sell  # i-1天的利润，相当于i+1天的cool down前的利润
            dp_sell = max(prices[i] + dp_buy, dp_sell)

        return dp_sell


class Solution714:
    # 含有手续费的
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell
