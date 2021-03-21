# 首先，如果数组中没有0的话，那么拥有最大乘积的子数组一定以原数组的第一个元素开始（前缀数组）或者以原数组的最后一个元素结尾（后缀数组）。
# 所以，我们分别计算前缀乘积数组和后缀乘积数组，也就是思路三中最终的数组nums和reverse_nums，然后返回两个数组中的最大值即可。
#
# 为什么这样呢？
#
# 假如说，我们有一个子数组A[i : j](i != 0, j != n) 并且子数组内的元素乘积为p。以P>0为例：如果 A[i] > 0 或A[j] > 0，
# 那么很明显，我们应该扩展这个子数组来包含A[i] 或 A[j]；
# 如果A[i] 和A[j]都是负数，那么应该扩展这个子数组包含A[i] 和A[j]来获得更大的乘积。重复这个过程，我们最终会到达原数组的开始或结尾。
#
# 如果原数组中有0怎么办？我们只需要把数组分割。也就是说，如果前缀数组乘积为0，我们重新从当前元素开始计算前缀乘积即可。
# 这也就是为什么nums[i] *= nums[i - 1] or 1
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)
