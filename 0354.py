import bisect
from typing import List


class Solution(object):
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
