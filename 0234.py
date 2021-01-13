# 回文链表


class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next

        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l = l + 1
            r = r - 1

        return True
