# 多数元素
# 排序 分治 哈希 随机化
import collections
from typing import List


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

    def majorityElement3(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


