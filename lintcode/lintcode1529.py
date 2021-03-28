# 使用双指针。初始化左指针left为0，右指针right为2。每次右指针移动一位，
# 指向三元组中最后一位元素，左指针向右移动到满足nums[right]-nums[left]<=limit为止。
# 如果right-left>=2，说明可以构成三元组，从nums[left, right-1]这个区间中任挑两位作为三元组的前两个元素，
# 有c(n,2)种选择。直到右指针遍历到最后一个元素为止。由于左右指针都只遍历了一次，所以时间复杂度为O(n)，空间复杂度为O(1)。


class Solution:
    """
    @param nums: the given array
    @param limit: the limit on the absolute difference of the subarray
    @return: Find the number of triplet subarray with the absolute difference less than or equal to limit
    """

    def tripletSubarray(self, nums, limit):
        left = 0
        res = 0
        mod = 99997867
        for right in range(2, len(nums)):
            while nums[right] - nums[left] > limit:
                left += 1
            if right - left >= 2:
                res += ((right - left) * (right - left - 1) // 2) % mod
        return res % mod
