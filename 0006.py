# z 字型变换

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [""] * numRows
        n = 2 * numRows - 2
        for i, char in enumerate(s):
            x = i % n
            rows[min(x, n - x)] += char
        return "".join(rows)


s = "PAYPALISHIRING"
numRows = 4
print(Solution().convert(s=s,numRows=numRows))
