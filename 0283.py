# 移动零
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for i, n in enumerate(filter(lambda x: x, nums)):
            nums[i] = n
        for i in range(i + 1, len(nums)):
            nums[i] = 0
