class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        for i in range(0, index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        # self.printList("addAtHead")

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        """if self.size == 0:
            node = ListNode(val)
            self.head = node
            return
        node = self.head
        for i in range(0, self.size-1):
            node = node.next
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
        """
        self.addAtIndex(self.size, val)
        # self.printList("addAtTail")

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        new_node = ListNode(val)
        node = self.head
        if index <= 0:
            new_node.next = node
            self.head = new_node
            self.size += 1
            return
        else:
            for i in range(0, index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
        self.size += 1
        # self.printList("addAtIndex")

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        node = self.head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        for i in range(0, index - 1):
            node = node.next
        node.next = node.next.next
        self.size -= 1
        # self.printList("deleteAtIndex")

    def printList(self, name):
        node = self.head
        print("Method called " + name)
        if node == None:
            print(" Head is none")
            return
        for i in range(0, self.size):
            print(str(node.val) + " ->")
            node = node.next
        print("...")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)