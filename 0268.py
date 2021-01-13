# 丢失的（缺失）数字 只有一个


class Solution:
    def missingNumber(self, nums):
        hashset = set([])
        for num in nums:
            hashset.add(num)
        for x in range(len(nums) + 1):
            if x not in hashset:
                return x


print(Solution().missingNumber(nums=[3, 0, 1]))
print(Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
