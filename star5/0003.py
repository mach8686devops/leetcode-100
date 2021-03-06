class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = ans = 0
        for i, c in enumerate(s):
            if c in hashmap:
                left = max(left, hashmap.get(c) + 1)
            hashmap[c] = i
            ans = max(ans, i - left + 1)
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])

            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # print(occ)
            # print(i, rk)
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        # print(occ)
        return ans


print(Solution().lengthOfLongestSubstring(s="pwwkew"))
