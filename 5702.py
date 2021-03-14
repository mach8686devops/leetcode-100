from collections import Counter
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = Counter()
        for u, v in edges:
            ans[u] += 1
            ans[v] += 1
        return ans.most_common(1)[0][0]
