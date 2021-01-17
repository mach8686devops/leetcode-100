from typing import List
import math
import collections


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0
        cnts = collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                cnts[nums[i] * nums[j]] += 1
        res = 0
        for k in cnts:
            if cnts[k] > 1:
                res += 8 * math.comb(cnts[k], 2)
        return res


# nums = [1, 2, 4, 5, 10]
nums = [2, 3, 4, 6, 8, 12]
print(Solution().tupleSameProduct(nums=nums))
