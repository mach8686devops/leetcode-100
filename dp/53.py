# 连续子数组的最大和
# 最大子数组
from typing import List


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        pos = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            pos = max(pos + nums[i], nums[i])
            ans = max(ans, pos)
        return ans

    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


nums = [-3, 1, 3, -1, 2, -4, 2]
print(Solution().maxSubArray(nums=nums))
print(Solution().maxSubArray2(nums=nums))
