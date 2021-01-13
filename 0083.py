# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next and head.val == head.next.val else head
