class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(n, -1, -1):
            pre = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + 1
                pre = temp
        return dp[-1]
