from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n, r = len(matrix), len(matrix) and len(matrix[0]), []
        for l in range(m + n - 1):
            temp = [matrix[i][l - i] for i in range(max(0, l + 1 - n), min(l + 1, m))]
            r += temp if l % 2 else temp[::-1]
        return r
