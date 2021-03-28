# 移动零
from typing import List


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for i, val in enumerate(filter(lambda x: x, nums)):
            nums[i] = val
        for i in range(i + 1, len(nums)):
            nums[i] = 0

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return 0
        # 两个指针i和j
        j = 0
        for i, val in enumerate(nums):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
