class Solution(object):
    # 快慢指针
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head and head.val is not None:
            head.val, head = None, head.next
        return head is not None
