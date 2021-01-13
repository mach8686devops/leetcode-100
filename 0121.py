from typing import List


class Solution:
    def maxProfit3(self, prices) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

    def maxProfit2(self, prices: List[int]) -> int:
        from functools import reduce
        return reduce(lambda r, p: (max(r[0], p - r[1]), min(r[1], p)), prices, (0, float('inf')))[0]

    def maxProfit(self, prices: List[int]) -> int:
        r, m = 0, float('inf')
        for p in prices:
            r, m = max(r, p - m), min(m, p)
        return r
