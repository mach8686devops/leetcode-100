import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums or target not in nums:  return [-1, -1]
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1] \
            if nums and target in nums else [-1, -1]
