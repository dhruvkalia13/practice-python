class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def is_empty(self):
        return self.__len__() == 0

    def push(self, val: int):
        self._stack.append(val)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        self._stack.pop()

    def top(self) -> int:
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self._stack[self.__len__() - 1]

    def print(self):
        print("Here's the stack")
        for item in self._stack:
            print(item)

    @property
    def stack(self):
        return self._stack
