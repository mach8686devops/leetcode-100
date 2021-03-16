class Solution:

    def __init__(self):
        self.delCost = 1
        self.insertCost = 2
        self.changeCost = 3

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]

    def edit(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = dp[i - 1][0] + self.delCost
        for j in range(m + 1):
            dp[0][j] = dp[0][j - 1] + self.insertCost

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + self.changeCost,  # 替换
                               dp[i][j - 1] + self.insertCost,  # 插入
                               dp[i - 1][j] + self.delCost)  # 删除
        print(dp)
        return dp[n][m]


word1 = "horse"
word2 = "ros"
print(Solution().edit(word1, word2))
