# 马拉车 一般不考
# 最长回文子串


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[1] * length for _ in range(length)]
        left, right = 0, 0  # 长度为1时
        for i in range(1, length):
            for j in range(length - i):
                if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
                    dp[j][j + i] = 1
                    left, right = j, j + i
                else:
                    dp[j][j + i] = 0
        return s[left: right + 1]


class Solution2:
    # 马拉车算法
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start + 1:end + 1:2]
