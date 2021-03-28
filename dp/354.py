import bisect
from typing import List


class Solution(object):

    # 此题 dp效果不佳
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]表示nums[i]这个数结尾的最长递增子序列的长度
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

    def maxEnvelopes(self, nums):

        nums.sort(key=lambda x: (x[0], -x[0]))
        print(nums)
        dpi = [i[1] for i in nums]
        print(dpi)
        return self.lengthOfLIS(dpi)


class Solution2(object):
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        lis = []
        for num in nums:
            insert_pos = bisect.bisect_left(lis, num)
            if insert_pos == len(lis):
                lis.append(num)
            else:
                lis[insert_pos] = num
        return len(lis)

    def maxEnvelopes(self, envs: List[List[int]]):
        n = len(envs)
        if n < 2:
            return n
        envs.sort(key=lambda t: (t[0], -t[1]))
        heights = [env[1] for env in envs]
        return self.lengthOfLIS(heights)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(Solution().maxEnvelopes(envelopes))
