class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return self.__len__() == 0

    def enqueue(self, val: int):
        self._queue.append(val)

    def dequeue(self):
        self._queue.pop(0)

    def print(self):
        print(self._queue)
