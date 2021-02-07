"""
Implementing queues using list
enqueue - append() : O(n) (adding at the end)
dequeue - pop(index) : O(n) (deletion from the beginning)
"""
a = []

a.append(1)
a.append(2)
a.append(3)

# print(a.pop(0))

########################################

"""
Implementing queues using collections.deque
Quicker append and pop from both ends
enqueue - append() : O(1)
dequeue - popleft() : O(1)
"""
from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

# print(q.popleft())
# print(q.pop())

########################################
from queue import Queue

b = Queue(maxsize=4) # maxsize = 0 (Infinite queue)

b.put(1)
b.put(2)
b.put(3)
b.put(4)
print(b.empty())
print(b.full())
print(b.get())
print(b.full())
print(b.get())
print(b.get())
print(b.get())
print(b.empty())


