# 反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList2(self, head: ListNode, tail=None) -> ListNode:
        if head: head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail

    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
