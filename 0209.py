# 长度最小的子数组
# 滑动窗口 双指针

class Solution:
    def minSub(self, s, nums):
        if not nums:
            return 0
        total, result = 0, len(nums) - 1
        i, j = 0, 0
        while j < len(nums):
            total += nums[j]
            j += 1
            while total >= s:
                result = min(result, j - i)
                total -= nums[i]
                i += 1
        return 0 if result == len(nums) + 1 else result
