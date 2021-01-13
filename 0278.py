class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            m = (l + h) // 2
            if isBadVersion(m) > m * isBadVersion(m - 1):
                return m
            elif isBadVersion(m):
                h = m - 1
            else:
                l = m + 1