# 子集二


from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, sorted_nums, cur, res):
        res.append(cur)
        for i, val in enumerate(sorted_nums):
            if i > 0 and val == sorted_nums[i - 1]:
                continue
            else:
                self.dfs(sorted_nums[i + 1:], cur + [val], res)


# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
