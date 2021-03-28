from typing import List


def helper(self, ns: List[int]):
    n = len(ns)
    dp = [[0] * n for _ in range(n + 1)]
    for l in range(n):  # 长度从小到大
        for i in range(n - l):  # 以 i 为 开头
            j = i + l  # 以 j 为 终点
            for k in range(i, j):  # 以 k 为分割点，进行分治
                # Todo 业务逻辑
                pass
                dp[i][k] = max(dp[i - 1][k], dp[i][k - 1])


# 依赖于前和下 可以从下到上、从前到后 或者 从前到后、从下到上
# 也可以 长度从短到长，相当于斜着来
class Solution:
    def PredictTheWinner(self, ns: List[int]) -> bool:
        n = len(ns)
        dp = [[0] * n for _ in range(n + 1)]
        for l in range(n):  # 长度从小到大
            for i in range(n - l):  # 以 i 为 开头的，l 为长度
                j = i + l
                dp[i][j] = max(ns[i] - dp[i + 1][j], ns[j] - dp[i][j - 1])
        return dp[0][-1] >= 0


# 依赖于 全部的长度1 需要用k进行枚举，只能先长度后起始点，相当于 斜线遍历
class Solution312:
    def maxCoins(self, ns: List[int]) -> int:
        ns = [1] + ns + [1]
        n = len(ns)
        dp = [[0] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                j = i + l
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + ns[i] * ns[k] * ns[j])
        return dp[0][-1]


# 与 312思想基本一致，枚举 k 时加一层限制
class Solution664:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n + 1)]
        for l in range(n):  # 区间长度
            for i in range(n - l):  # 区间起点
                j = i + l  # 区间终点
                dp[i][j] = dp[i + 1][j] + 1  # 初始化
                for k in range(i + 1, j + 1):  # 枚举分割点
                    if s[k] == s[i]:  # 首位一样可减少一次
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
        return dp[0][-1]


# 依赖于 全部的长度1 及 尾部状态
class Solution546:
    def removeBoxes(self, bs: List[int]) -> int:
        n = len(bs)
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        for l in range(n):  # l++ 从小段 到 大段
            for i in range(n - l):  # i++ 起点 从小到大
                j = i + l
                for t in range(n - j):  # 尾部tail 同数 从小 到 大
                    dp[i][j][t] = max(dp[i][j][t], dp[i][j - 1][0] + pow(t + 1, 2))
                    for k in range(i, j):  # 枚举 分割点 k
                        if bs[k] == bs[j]:
                            dp[i][j][t] = max(dp[i][j][t],
                                              dp[i][k][t + 1] + dp[k + 1][j - 1][0])
        return dp[0][n - 1][0]
