# 四数之和
# 枚举前两个数 哈希后两个
import collections
from typing import List


class Solution:
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        from itertools import combinations as com
        dic, l = collections.defaultdict(list), [*com(range(len(nums)), 2)]
        for a, b in l: dic[target - nums[a] - nums[b]].append((a, b))
        r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]
        return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        len_nums = len(nums)

        # hash后两个数的和，并保存索引
        table = {}
        for j in range(len_nums - 1, 2, -1):
            if j < len_nums - 1 and nums[j] == nums[j + 1]:
                continue
            if 4 * nums[j] < target:
                break
            if nums[j] + 3 * nums[0] > target:
                continue
            for i in range(j - 1, 1, -1):
                if i < j - 1 and nums[i] == nums[i + 1]:
                    continue
                if nums[j] + 3 * nums[i] < target:
                    break
                if nums[j] + nums[i] + 2 * nums[0] > target:
                    continue
                table.setdefault(nums[i] + nums[j], []).append((i, j))

        # 枚举前两个数
        for i in range(len_nums - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[i] + 3 * nums[-1] < target:
                continue
            for j in range(i + 1, len_nums - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + 3 * nums[j] > target:
                    break
                if nums[i] + nums[j] + 2 * nums[-1] < target:
                    continue
                for index, jndex in table.get(target - nums[i] - nums[j], []):
                    if j < index:
                        ans.append([nums[i], nums[j], nums[index], nums[jndex]])

        return ans


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
