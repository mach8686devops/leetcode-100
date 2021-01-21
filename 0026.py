from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1 if nums else 0

    def removeDuplicates2(self, nums: List[int]) -> int:
        n = len(nums)
        slow, fast = 0, 1
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1 if nums else 0
