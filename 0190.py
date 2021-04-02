class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits2(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits(self, n: int) -> int:
        # return int(bin(n)[2:].zfill(32)[::-1], 2)
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
