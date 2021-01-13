class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        prev = -1
        for i, val in enumerate(nums):
            if val == target:
                return i
            elif val < target:
                prev = i
            else:
                return prev + 1

        return prev + 1

    def search(self, nums, target):
        if not nums:
            return 0
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
