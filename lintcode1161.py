class Solution:
    """
    @param n: the number of backpacks
    @param a: the number of goods each backpack carries
    @param b:  the maximum capacity of each backpack
    @return: given n, ai and bi,return the minimum number of backpacks and the minimum time
    """

    def goodsTransfer(self, n, a, b):
        # write your code here
        INF = 0x3f3f3f3f
        k = INF
        sum_good = 0
        sum_cap = 0
        max_weight = 0
        for good in a:
            sum_good += good
        for cap in b:
            sum_cap += cap
        dp = [INF for _ in range(sum_cap + 1)]
        weight = [0 for _ in range(sum_cap + 1)]
        dp[0] = 0
        for i in range(n):
            j = sum_cap
            while j > 0:
                res = max(j - b[i], 0)
                if dp[j] < dp[res] + 1:
                    j -= 1
                    continue
                if dp[j] > dp[res] + 1:
                    dp[j] = dp[res] + 1
                    weight[j] = weight[res] + a[i]
                else:
                    weight[j] = max(weight[j], weight[res] + a[i])
                j -= 1
        for i in range(sum_good, sum_cap + 1):
            if dp[i] < k:
                k, max_weight = [dp[i], weight[i]]
            elif dp[i] == k:
                max_weight = max(max_weight, weight[i])
        return [k, sum_good - max_weight]
