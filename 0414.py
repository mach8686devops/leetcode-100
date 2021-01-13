class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        for _ in range((2, 0)[len(nums) < 3]): nums.remove(max(nums))
        return max(nums)
