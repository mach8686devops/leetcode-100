# 编辑距离

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mem = {}

        def dp(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                mem[(i, j)] = dp(i - 1, j - 1)
            else:
                mem[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i - 1, j - 1) + 1
                )
            return mem[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

# 从二维的空间是否可以到一维度的空间 节省一些
