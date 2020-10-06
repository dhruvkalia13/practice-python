from queues import queue_using_array

queue = queue_using_array.Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(1)
queue.dequeue()
queue.dequeue()

queue.print()
