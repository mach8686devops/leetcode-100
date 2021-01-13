from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return os.path.commonprefix(strs)
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return strs[0][:r.index(0)] if strs else ''
