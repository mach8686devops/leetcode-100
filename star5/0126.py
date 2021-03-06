import collections
import string
from typing import List


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)

        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for i in range(n):
                    first, second = x[:i], x[i + 1:]
                    for c in string.ascii_lowercase:
                        y = first + c + second
                        if y in words:
                            if y in eq:
                                found = True
                            else:
                                nq.add(y)
                            tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            if x == endWord:
                return [[x]]
            return [[x] + rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)


class Solution2(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)  # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]]  # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord:
                    return layer[word]  # return all found sequences
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    # for c in 'abcdefghijklmnopqrstuvwxyz':
                    first, second = word[:i], word[i + 1:]
                    for c in string.ascii_lowercase:
                        newWord = first + c + second
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[
                                word]]  # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops
            layer = newlayer  # move down to new layer

        return []
