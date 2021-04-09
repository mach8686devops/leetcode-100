def search(nums: [int], target: int) -> bool:
    # return target in nums
    if not nums:
        return False
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] == target:
            return True
        if nums[left] == nums[right]:
            left += 1
            continue
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return False
