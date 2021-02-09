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
q.append(9)
q.append(2)
q.append(1)
q.append(4)
q.append(8)
q.append(7)
print(q[0])

# q_sorted = deque(sorted(q, key=lambda x: q.index(x) % 2))
# a = deque()
# a.append(4)
# a.append(5)
# a.append(6)

# q.extendleft(a)
# print(q)
# print(q_sorted)
# print(q.popleft())
# print(q)
# print(q.pop())
# a = float('inf')
# print(a)

