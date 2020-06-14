# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        fastA = headA
        fastB = headB
        while fastA != fastB:
            fastA = fastA.next if fastA != None else headB
            fastB = fastB.next if fastB != None else headA
        return fastA