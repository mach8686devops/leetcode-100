import collections
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

        d = collections.defaultdict(int)
        d[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            p = releaseTimes[i] - releaseTimes[i - 1]
            if keysPressed[i] not in d:
                d[keysPressed[i]] = p
            else:
                if p > d[keysPressed[i]]:
                    d[keysPressed[i]] = p
        t = list(d.items())
        t.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return t[0][0]


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"

print(Solution().slowestKey(releaseTimes=releaseTimes, keysPressed=keysPressed))
