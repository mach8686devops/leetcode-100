# 不要使用额外的数组空间 原地修改输入数组
# 双指针 移除元素


class Solution:
    def removeElement(self, nums, target):
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] != target:
                l += 1
            while l < r and nums[r] == target:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]

        return l if nums[l] == target else l + 1


print(Solution().removeElement(nums=[3, 2, 2, 3], target=3))
print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], target=2))
