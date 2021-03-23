import bisect
from typing import List


class Solution(object):
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def lengthOfLIS(self, A: List[int]) -> int:
        d = []
        for a in A:
            i = bisect.bisect_left(d, a)
            if i < len(d):
                d[i] = a
            elif not d or d[-1] < a:
                d.append(a)
        return len(d)
