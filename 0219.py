from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r, d = k + 1, {}
        for i, n in enumerate(nums):
            r, d[n] = min(r, i - d.get(n, -k - 1)), i
        return r <= k
