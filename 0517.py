# 超级洗衣机


class Solution(object):
    def findMinMoves(self, a):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(a) % len(a) != 0:
            return -1
        avg = sum(a) // len(a)
        ans = s = 0
        for i in a:
            s += i - avg
            ans = max(ans, abs(s), i - avg)

        return ans
