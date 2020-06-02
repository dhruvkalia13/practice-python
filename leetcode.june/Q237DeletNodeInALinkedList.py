# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        # node.val = curr.next.val
        # node.next = curr.next
        while curr is not None:
            curr.val = curr.next.val
            if curr.next.next is None:
                curr.next = None
                break
            else:
                curr = curr.next


