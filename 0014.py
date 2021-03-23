from typing import List


class Solution:
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # return os.path.commonprefix(strs)
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''

    # 先排序
    # 计算相邻的
    # 长度放到线段树
    # 查询两个字符串的最长公共前缀
    # 线段树 SegmentTree

    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n - 1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
