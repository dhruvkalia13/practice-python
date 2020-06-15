# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        # 1 2 3 4 5
        # 2 1 3 4 5
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = head
            head = temp
        return head
