
from typing import List
from collections import Counter
from itertools import combinations
from functools import lru_cache


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:

        @lru_cache(None)
        def dp(status):
            if status == target:
                return 0
            avl = []  # store the index of the available keys
            for i, v in enumerate(status):
                if v < counts[keys[i]]:
                    avl.append(i)
            res = float('inf')
            for combs in combinations(avl, each_group):  # try all the combinations of the available keys
                s2 = list(status)
                max_v, min_v = float('-inf'), float('inf')
                for c in combs:
                    s2[c] += 1
                    max_v = max(max_v, keys[c])
                    min_v = min(min_v, keys[c])
                res = min(res, max_v - min_v + dp(tuple(s2)))
            return res

        len_n = len(nums)
        counts = Counter(nums)
        # 剪枝
        if max(counts.values()) > k:
            return -1
        target = tuple(counts.values())
        keys = list(counts.keys())
        len_c = len(counts)
        each_group = len_n // k

        return dp(tuple([0] * len_c))

