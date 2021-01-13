# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]


from typing import List


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         cha = list(set(arr1).difference(set(arr2)))
#         # print(cha)
#         res = []
#         for _, x in enumerate(arr1):
#             if x in arr2:
#                 res.append(x)
#         print(res)
#         ans = res+cha
#         print(ans)

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1

        ans = []
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

print(Solution().relativeSortArray(arr1, arr2))
