import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dic = collections.Counter(a + b for a in A for b in B)
        return sum(dic.get(- c - d, 0) for c in C for d in D)
