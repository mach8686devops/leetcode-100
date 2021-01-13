from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]
