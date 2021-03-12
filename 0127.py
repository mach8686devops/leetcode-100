import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()
            print(word, length)
            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        queue.append((next_word, length + 1))
                        wordList.remove(next_word)

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
