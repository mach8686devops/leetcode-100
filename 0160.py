# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = (headA, headB) if headA and headB else (None, None)
        while a != b: a, b = not a and headB or a.next, not b and headA or b.next
        return a