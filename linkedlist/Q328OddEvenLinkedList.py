# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, evenHead = ListNode(0), ListNode(0)
        start = odd
        even = evenHead
        curr = head
        isOdd = True
        while curr:
            if isOdd:
                odd.next = curr
                odd = odd.next
            else:
                evenHead.next = curr
                evenHead = evenHead.next
            isOdd = not isOdd
            curr = curr.next
        evenHead.next = None
        odd.next = even.next
        return start.next