class Solution:
    def findPoisonedDuration(self, t: List[int], d: int) -> int:
        return len(t) and sum(min(t[i] - t[i-1], d) for i in range(1, len(t))) + d