class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ou = [i for i in A if i & 1]
        ji = [i for i in A if not i & 1]
        return [i for n in zip(ji, ou) for i in n]


print(Solution().sortArrayByParityII(A=[4,2,5,7]))