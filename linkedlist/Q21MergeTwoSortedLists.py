# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # [1, 2, 4]
    # [1, 3, 4]
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head1 = l1
        head2 = l2
        head3 = ListNode(-1)
        i = 0
        out = ListNode(-1)
        while head1 or head2:
            if head1 and head2:
                if head1.val < head2.val:
                    n = ListNode(head1.val)
                    head3.next = n
                    head1 = head1.next
                    head3 = n
                    if i == 0:
                        out = n
                        i += 1
                    continue
                else:
                    n = ListNode(head2.val)
                    head3.next = n
                    head2 = head2.next
                    head3 = n
                    if i == 0:
                        out = n
                        i += 1
                    continue
            if head1 and head2 is None:
                n = ListNode(head1.val)
                head3.next = n
                head1 = head1.next
                head3 = n
                if i == 0:
                    out = n
                    i += 1
                continue
            if head2 and head1 is None:
                n = ListNode(head2.val)
                head3.next = n
                head2 = head2.next
                head3 = n
                if i == 0:
                    out = n
                    i += 1
                continue
        return out



