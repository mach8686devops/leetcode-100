
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        r, odd, p, head = head, head, head.next, head.next.next
        while head:
            odd.next, head.next, p.next = head, odd.next, head.next
            p, odd, head = p.next, head, p.next and p.next.next
        return r