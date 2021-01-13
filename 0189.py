from typing import List


class Solution:
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k % len(nums)): nums[-1:], nums[:0] = [], nums[-1:]
