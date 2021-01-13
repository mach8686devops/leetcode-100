class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head: head.next = self.removeElements(head.next, val)
        return head.next if head and head.val == val else head