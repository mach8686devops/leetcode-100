class Solution:
    """
    @param str: The string before proofreading.
    @return: Return the string after proofreading.
    """

    def automaticProofreadingProgram(self, str):
        result = []

        for c in str:
            result.append(c)
            # 规则1
            if len(result) >= 3:
                if result[-1] == result[-2] == result[-3]:
                    result.pop()

            # 规则2
            if len(result) >= 4:
                if result[-1] == result[-2] and result[-3] == result[-4]:
                    result.pop()

        return "".join(result)
