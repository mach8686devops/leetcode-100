class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """

    def FinalDiscountedPrice(self, prices):
        # write your code here
        n = len(prices)
        s, res = [], [prices[i] for i in range(n)]

        for i in range(n):
            while s and prices[s[-1]] >= prices[i]:
                index = s[-1]
                s.pop()
                res[index] = prices[index] - prices[i]
            s.append(i)
        return res


prices = [2, 3, 1, 2, 4, 2]
print(Solution().FinalDiscountedPrice(prices))
