class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(len(s), -1, -1):
            pre = 0
            for j in range(i + 1, len(s)):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + 1
                pre = temp
        return dp[-1]
