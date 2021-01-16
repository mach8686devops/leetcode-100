from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = Counter(arr)
        print(s)
        for n in s:
            if n == 0:
                if s[n] > 1:
                    return True
            elif n << 1 in s:
                return True
        return False

    def checkIfExist2(self, arr: List[int]) -> bool:
        pass
        Hash = {}
        for i in arr:
            Hash[i] = Hash.get(i, 0) + 1
        # print(Hash)
        for i in arr:
            if Hash.get(i * 2):
                if i * 2 == 0:
                    if Hash.get(0) > 1:
                        return True
                return True
        return False


print(Solution().checkIfExist2(arr=[7, 1, 14, 11]))
