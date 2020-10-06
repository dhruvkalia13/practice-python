from queues.Queue_using_linked_list.Node import Node

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def dequeue(self):
        h = self.head
        if self.head is None:
            print("the queue is empty")
            return
        while h.next is not None:
            if h.next.next is None:
                rem = h.next
                h.next = None
                return rem
            h = h.next

    def print(self):
        temp = self.head
        print("Here's the queue")
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        print(temp.val)