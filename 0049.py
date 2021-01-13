# 字母异位词分组


class Solution:
    def group(self, strs):
        if len(strs) < 2:
            return strs
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            ans[key] = ans.get(key, []) + [s]
        return ans.values()
        # return [[*x] for _, x in itertools.groupby(sorted(strs, key=sorted), sorted)]
