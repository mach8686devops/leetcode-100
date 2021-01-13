class Solution:
    def wordBreak(self, s, wordDict):

        def f(s, d={}):
            if not s in d:
                for i in range(1, 1 + len(s)):
                    d[s[:i]] = s[:i] in wordDict and (i == len(s) or f(s[i:]))
                    if d[s[:i]]: return True
                return False
            return d[s]

        return f(s)

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True

        breakp = [0]

        for i in range(len(s) + 1):
            for j in breakp:
                if s[j:i] in wordDict:
                    breakp.append(i)
                    break
        print(breakp)
        return breakp[-1] == len(s)


s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak2(s=s, wordDict=wordDict))
