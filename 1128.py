from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = dict(Counter(tuple(sorted(d)) for d in dominoes))
        print([n if n >= 2 else 0 for n in c.values()])

        return sum(
            c * (c - 1)
            for c in Counter(
                tuple(sorted(d))
                for d in dominoes
            ).values()
        ) // 2


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
print(Solution().numEquivDominoPairs(dominoes))
