import bisect
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.__class__.__getitem__ = lambda self, i: i and nums[i - 1] > nums[i]
        return bisect.bisect_left(self, True, 0, len(nums)) - 1