class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(cur, i, d={}):
            if i < len(nums) and (i, cur) not in d:  # 搜索周围节点
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0)