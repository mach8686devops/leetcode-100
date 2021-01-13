class Solution(object):
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
        while head and head.val != None: head.val, head = None, head.next
        return head != None