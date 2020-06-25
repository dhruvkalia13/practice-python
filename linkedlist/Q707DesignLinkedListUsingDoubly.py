class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        curr = self.head
        for i in range(self.size):
            if i == index:
                return curr.val
            curr = curr.next
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        end = False
        curr = self.head
        new = ListNode(val)
        if curr is None:
            self.head = new
            self.size += 1
            self.printList()
            return
        if index == 0:
            new.next = curr
            curr.prev = new
            self.head = new
            self.size += 1
            self.printList()
            return
        if index == self.size:
            end = True
        i = 0
        while curr:
            if end and i == self.size:
                new.prev = curr
                curr.next = new
                self.size += 1
                self.printList()
                return
            elif end:
                curr = curr.next if curr.next else curr
                i += 1
                continue
            elif i == index:
                previous = curr.prev
                previous.next = new
                new.prev = previous
                new.next = curr
                curr.prev = new
                self.size += 1
                self.printList()
                return
            else:
                curr = curr.next if curr.next else curr
                i += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        end = False
        print("After deletion")
        if self.size <= 0 or index >= self.size or index < 0:
            print("Not found")
            return
        curr = self.head
        if self.size == 1:
            self.head = None
            self.size -= 1
            self.printList()
            return
        if index == 0:
            next_ele = curr.next
            next_ele.prev = None
            self.head = next_ele
            self.size -= 1
            self.printList()
            return
        if index == self.size-1:
            end = True
        i = 0
        while curr:
            if end and i == self.size - 1:
                previous = curr.prev
                previous.next = None
                self.size -= 1
                self.printList()
                return
            elif end:
                curr = curr.next if curr.next else curr
                i += 1
                continue
            if i == index:
                previous = curr.prev
                next_ele = curr.next
                previous.next = next_ele
                next_ele.prev = previous
                curr.prev, curr.next = None, None
                self.size -= 1
                self.printList()
                return
            curr = curr.next if curr.next else curr
            i += 1

    def printList(self):
        print("Size is " + str(self.size))
        print("List is ")
        curr = self.head
        while curr:
            print(str(curr.val))
            curr = curr.next
        print("...")


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
param_1 = obj.get(5)
print("param_1 is " + str(param_1))
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)