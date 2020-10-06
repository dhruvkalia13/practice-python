from stack.Stack_using_array.stack_using_array import Stack

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.print()
stack.pop()
stack.print()
stack.push(99)
stack.print()
print("top ele is " + str(stack.top()))