# 子集
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        return sum([list(combinations(nums, i)) for i in range(len(nums) + 1)], [])

    def subsets2(self, nums):
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, cur):
        res.append(cur)
        for i, val in enumerate(nums):
            self.dfs(nums[i + 1:], res, cur + [val])


print(Solution().subsets(nums=[1, 2, 3]))
