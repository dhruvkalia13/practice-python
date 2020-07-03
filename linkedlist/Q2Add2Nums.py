# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(-1)
        i = 0
        res = ListNode(-1)
        carry = 0
        while l1 or l2:
            if l1 and not l2:
                out = l1.val + carry
            elif l2 and not l1:
                out = l2.val + carry
            elif l1 and l2:
                out = l1.val + l2.val + carry

            if carry == 1:
                carry = 0
            if out > 9:
                carry = 1
                out = out % 10
            n = ListNode(out)
            l3.next = n
            if i == 0:
                res = l3
                i += 1
            l3 = n
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            n = ListNode(1)
            l3.next = n
            if i == 0:
                res = l3
                i += 1
            l3 = n
        return res.next
