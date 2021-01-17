import collections
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        row, col = len(matrix), len(matrix[0])
        res = 0
        for r in range(row):
            cnts = collections.defaultdict(int)
            for c in range(col):
                if matrix[r][c] == 1:
                    dp[r, c] = 1 + dp[r - 1, c]
                    res = max(res, dp[r, c])
                    cnts[dp[r, c]] += 1
            sm = 0
            for k in sorted(cnts.keys())[::-1]:
                sm += cnts[k]
                res = max(res, sm * k)
        return res
