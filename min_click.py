#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
题目： 阿里云题目，数据中元素代表线段起始点和终点， 点击线段内任意一点，即可消除线段，求最少点击数能消除所有线段
"""


def min_click(nums):
    """
    思路： 与 leetcode 56相似
          区别
            - 为只返回点击数量，不需要保存所有数组，
            - 遍历时两区间的交集（而非并集合）与一下 区间进行对比
    """
    if not nums:
        return 0

    nums.sort(key=lambda s: s[0])
    count, prev = 1, nums[0]

    for cur in nums[1:]:
        print(prev, cur, count)
        if cur[0] > prev[1]:  # 不相交
            count += 1
            prev = cur
        else:
            prev = [cur[0], min(cur[1], prev[1])]

    return count


if __name__ == '__main__':
    nums = [[4, 8], [2, 8], [5, 9], [10, 12]]
    # nums = [[4, 8], [2, 8], [5, 9], [7, 12]]
    result = min_click(nums)
    print(f"result is {result}")
