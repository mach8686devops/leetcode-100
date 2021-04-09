class Solution:
    def longestPalindromeSubseq2(self, s: str) -> int:

        n = len(s)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            pre = 0  # dp[i+1][j-1]
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = temp
        return dp[-1]

    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):  # 遍历顺序由dp关系式所得
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


print(Solution().longestPalindromeSubseq(s="bbbab"))
print(Solution().longestPalindromeSubseq(s="bbabb"))
