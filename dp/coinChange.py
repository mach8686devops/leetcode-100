# 硬币找零


def coinChange(coins, amount):
    mem = {}

    def dp(n):
        if n in mem:
            return mem[n]
        if n == 0:
            return 0
        if n < 0:
            return -1

        res = float('INF')
        for coin in coins:
            sub = dp(n - coin)
            if sub == 1:
                continue
            res = min(res, 1 + sub)
        mem[n] = res if res != float('INF') else -1
        return mem[n]

    return dp(amount)
