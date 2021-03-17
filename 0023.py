from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        r, n, p = [], lists and lists.pop(), None
        while lists or n:
            r[len(r):], n = ([n], n.next or lists and lists.pop()) if n else ([], lists.pop())
        for n in sorted(r, key=lambda x: x.val, reverse=True):
            n.next, p = p, n
        return n if r else []

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
