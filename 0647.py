class Solution:
    def __init__(self):
        self.res = 0

    def countSubstrings(self, s: str) -> int:
        l = len(s)
        for i in range(l):
            self.expand(i, i, s)  # 以单个字符拓展
            if i + 1 < l and s[i] == s[i + 1]:
                self.expand(i, i + 1, s)  # 以两个字符拓展
        return self.res

    def expand(self, i, j, s):
        self.res += 1  # 单个字符或者相等的两个字符本身就是回文字符串
        while i - 1 >= 0 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
            i, j = i - 1, j + 1
            self.res += 1


