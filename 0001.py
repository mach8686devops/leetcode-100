# 两数之和
#  哈希表
# from threading import Semaphore


class Solution:
    def twoSum(self, nums, target):
        mapping = {}
        for i, item in enumerate(nums):
            if (target - item) in mapping:
                return [mapping[target - item], i]
            mapping[item] = i
        # 注意是否有一定能够找到的条件
        # return [-1, -1]

    def twoSum2(self, numbers, target):
        if not numbers:
            return [-1, -1]

        # transform numbers to a sorted array with index
        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        nums = sorted(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])

        return [-1, -1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
