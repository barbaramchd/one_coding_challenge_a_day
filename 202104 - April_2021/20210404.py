"""
  Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.my_queue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.my_queue) < self.k:
            self.my_queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.my_queue:
            self.my_queue.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        if self.my_queue:
            return self.my_queue[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.my_queue:
            return self.my_queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.my_queue) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.my_queue) == self.k:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()