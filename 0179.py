class compare(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest = sorted([str(v) for v in nums], key=compare)  # 排序
        print(largest)
        largest = ''.join(largest)  # 转换字符串

        return '0' if largest[0] == '0' else largest  # 如果第一个值为0，很显然，后面有的话也是0，直接


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
