# 马拉车 一般不考
# 最长回文子串

# 实现中心扩展法


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        if n < 2:
            return s
        for i in range(n - 1):
            oddstr = self.extend(s, i, i)
            evenstr = self.extend(s, i, i + 1)
            temp = oddstr if len(oddstr) > len(evenstr) else evenstr
            if len(temp) > len(res):
                res = temp

        return res

    def extend(self, s: str, i, j) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j]


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


class Solution4(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 2:
            return s

        # 以left和right为起点，计算回文半径，由于while循环退出后left和right
        # 各多走了一步，所以在返回的总长度时要减去2
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right - left - 2) // 2

        # 对原始字符串做处理，将abc变成#a#b#c#
        tmp = "#" + "#".join(list(s)) + "#"
        n = len(tmp)
        start = 0
        maxLen = 0
        # right表示目前计算出的最右端范围，right和左边都是已探测过的
        right = 0
        # center最右端位置的中心对称点
        center = 0
        # p数组记录所有已探测过的回文半径，后面我们再计算i时，根据p[i_mirror]计算i
        p = [0] * n
        # 从左到右遍历处理过的字符串，求每个字符的回文半径
        for i in range(n):
            # 根据i和right的位置分为两种情况：
            # 1、i<=right利用已知的信息来计算i
            # 2、i>right，说明i的位置时未探测过的，只能用中心探测法
            if right >= i:
                # 这句是关键，不用再像中心探测那样，一点点的往左/右扩散，根据已知信息
                # 减少不必要的探测，必须选择两者中的较小者作为左右探测起点
                minArmLen = min(right - i, p[2 * center - i])
                p[i] = expand(tmp, i - minArmLen, i + minArmLen)
            else:
                # i落在right右边，是没被探测过的，只能用中心探测法
                p[i] = expand(tmp, i, i)
            # 大于right，说明可以更新最右端范围了，同时更新center
            if i + p[i] > right:
                center = i
                right = i + p[i]
            # 找到了一个更长的回文半径，更新原始字符串的start位置
            if p[i] > maxLen:
                start = (i - p[i]) // 2
                maxLen = p[i]
        # 根据start和maxLen，从原始字符串中截取一段返回
        return s[start: start + maxLen]
