class MKAverage:

    def __init__(self, m: int, k: int):
        self.ans = []
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.ans.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.ans) < self.m:
            return -1

        middle = self.ans[-self.m:]
        middle.sort()
        return sum(middle[self.k:len(middle) - self.k]) // (len(middle) - 2 * self.k)
