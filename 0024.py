# 两两交换链表节点


class Solution:
    def swapPairs(self, head):
        if head and head.next:
            head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
        # if not head or not head.next:
        #     return head
        # nxt = head.next
        # head.next = self.swap_pair(head.next.next)
        # nxt.next = head
        # return nxt
