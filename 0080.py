def removeDuplicates(nums: [int]) -> int:
    for i in range(len(nums) - 3, -1, -1):
        if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
            nums.pop(i)
    return len(nums)
