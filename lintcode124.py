class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longestConsecutive(self, num):
        # write your code here
        dic = {}

        for x in num:
            dic[x] = 1

        ans = 0

        for x in num:
            if x in dic:
                length = 1
                del dic[x]
                l = x - 1
                r = x + 1
                while l in dic:
                    del dic[l]
                    l -= 1
                    length += 1
                while r in dic:
                    del dic[r]
                    r += 1
                    length += 1
                if ans < length:
                    ans = length

        return ans
