from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur = {k: 1}
        res = 0
        s = 0
        for num in nums:
            s += num
            temp = occur.get(s, 0)
            res += temp
            occur[s + k] = occur.get(s + k, 0) + 1
        return res
