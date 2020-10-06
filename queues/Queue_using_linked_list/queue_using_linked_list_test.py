from queues.Queue_using_linked_list.queue_using_linked_list import Queue

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
queue.print()
print("Returned element is " + str(queue.dequeue().val))
queue.print()
queue.enqueue(99)
queue.print()
print("Returned element is " + str(queue.dequeue().val))
queue.print()