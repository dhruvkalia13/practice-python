# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(1, n+2):
            slow = slow.next
        while slow:
            fast = fast.next
            slow = slow.next
        fast.next = fast.next.next
        return dummy.next