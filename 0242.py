from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # O(n) 思路等于建哈希表

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # O(n log(n)) 排序后相等，原来就相等，利用 python 的 str 可以直接排序的特点
