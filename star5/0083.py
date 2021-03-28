# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        if head:
            head.next = self.deleteDuplicates2(head.next)
            return head.next if head.next and head.val == head.next.val else head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        # 断开与重复元素的连接
        slow.next = None
        return head
