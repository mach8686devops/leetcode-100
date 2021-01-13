import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = [x for x in nums if x > nums[0]]
        m = [x for x in nums if x == nums[0]]
        r = [x for x in nums if x < nums[0]]
        f = self.findKthLargest

        if k <= len(l):
            return f(l, k)
        elif k <= len(l) + len(m):
            return nums[0]
        return f(r, k - len(l) - len(m))

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
