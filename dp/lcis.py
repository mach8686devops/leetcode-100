from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化
        dp = [1] * n
        if not nums:
            return 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

    def findLengthOfLCIS2(self, nums: List[int]) -> int:
        ans, anchor = 0, 0
        n = len(nums)
        for i in range(n):
            if i and nums[i] <= nums[i - 1]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


print(Solution().findLengthOfLCIS(nums=[1, 3, 5, 4, 7]))
