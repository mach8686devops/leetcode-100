import bisect
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        self.__class__.__getitem__ = lambda sef, m: sum(n <= m for n in nums) > m
        return bisect.bisect_left(self, True, 1, len(nums) - 1)
