from stack.Stack_using_linked_list.stack_using_linked_list import Stack

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.print()
stack.pop()
stack.print()
stack.push(99)
stack.print()
print("top ele is " + str(stack.top().val))