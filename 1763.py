class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = set(s)
        for ch in s:
            if ch.swapcase() not in d:
                return max((self.longestNiceSubstring(t) for t in s.split(ch)), key=len)
        return s
