import bisect


class Solution:
    def search(self, nums, target):
        lo, hi, k = 0, len(nums) - 1, -1
        while lo <= hi:
            m = (lo + hi) // 2
            if m == len(nums) - 1 or nums[m] > nums[m + 1]:
                k = m + 1
                break
            elif m == 0 or nums[m] < nums[m - 1]:
                k = m
                break
            if nums[m] > nums[0]:
                lo = m + 1
            else:
                hi = m - 1
        i = (bisect.bisect_left(nums[k:] + nums[:k], target) + k) % max(len(nums), 1)
        return i if nums and nums[i] == target else -1
