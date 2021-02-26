import itertools

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        if len(nums) <= 0:
            return []
        return list(set(itertools.permutations(nums, len(nums))))
