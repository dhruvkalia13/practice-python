from customlinkedlist.Node import Node


class CustomLinkedList:
    head = None

    def insert(self, list, value):
        new_node = Node(value)
        new_node.next = None
        if list.head == None:
            list.head = new_node
        else:
            last = list.head
            while last.next is not None:
                last = last.next
            last.next = new_node
        print("value %d added" % value)
        return list

    def printList(self, list):
        current = list.head
        print("Here is the list")
        while current is not None:
            print(current.val)
            current = current.next

    def remove(self, list, value):
        current = list.head
        if current.val is value:
            list.head = current.next
            print("%d is removed from the list" % value)
            return
        while current.next is not None:
            nxt = current.next
            if nxt.val is value:
                #found
                current.next = nxt.next
                print("%d is removed from the list" % value)
                return
            current = current.next
        print("value %d not found in list" % value)


    def removeAll(self, list):
        list.head = None
        print("list is not empty")

    def length(self, list):
        current = list.head
        length = 0
        while current is not None:
            length = length + 1
            current = current.next
        return length

    def find(self, list, value):
        current = list.head
        pos = 0
        while current is not None:
            if current.val is value:
                #found
                return pos
            pos = pos + 1
            current = current.next
        return -1
