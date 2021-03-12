# 递归 两数相加
# 链表


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        ans = l1.val + l2.val
        # 地板除 余
        digit = ans // 10
        remain = ans % 10
        res = ListNode(remain)
        if l1.next or l2.next or digit:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += digit
            res.next = self.addTwoNumbers(l1, l2)
        return res
        # if not (l1 or l2):
        #     return ListNode(1) if carry else None
        # l1, l2 = l1 or ListNode(0), l2 or ListNode(0)
        # val = l1.val + l2.val + carry
        # l1.val, l1.next = val % 10, self.addTwoNumbers(l1.next, l2.next, val > 9)
        # return l1
