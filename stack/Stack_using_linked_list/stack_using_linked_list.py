from stack.Stack_using_linked_list.Node import Node


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, val: int):
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> Node:
        if self.head is None:
            print("Stack is empty")
            return Node(-1)
        else:
            rem_node = self.head
            self.head = rem_node.next
            rem_node.next = None
            return rem_node

    def top(self) -> Node:
        if self.head is None:
            print("Stack is empty")
            return Node(-1)
        else:
            return self.head

    def print(self):
        temp = self.head
        print("Here's the stack")
        while temp.next is not None:
            print(temp.val)
            temp = temp.next
        print(temp.val)
