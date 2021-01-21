from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        r, n, p = [], lists and lists.pop(), None
        while lists or n:
            r[len(r):], n = ([n], n.next or lists and lists.pop()) if n else ([], lists.pop())
        for n in sorted(r, key=lambda x: x.val, reverse=True):
            n.next, p = p, n
        return n if r else []
