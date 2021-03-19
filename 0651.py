# 四键键盘

# A键
# C-A 全选
# C-C
# C-V


class Solution:
    def maxA2(self, N):
        mem = {}

        def dp(n, a_num, copy):
            if n <= 0:
                return a_num
            if (n, a_num, copy) in mem:
                return mem[(n, a_num, copy)]
            mem[(n, a_num, copy)] = max(dp(n - 1, a_num + 1, copy),  # A
                                        dp(n - 1, a_num + copy, copy),  # C-V
                                        dp(n - 2, a_num, a_num)  # C-A C-C
                                        )
            return mem[(n, a_num, copy)]

        return dp(N, 0, 0)

    def maxA(self, N):
        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(1, N + 1):
            # A 键
            dp[i] = dp[i - 1] + 1
            # C-V
            for j in range(2, i):
                # 全选复制 连续粘贴
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))

        return dp[-1]


print(Solution().maxA(N=7))
