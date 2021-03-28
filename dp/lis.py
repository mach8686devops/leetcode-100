from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # 初始化并且定义dp
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 自对抗储存前面大的
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)  # 万一前面已经结束且比末元素大
