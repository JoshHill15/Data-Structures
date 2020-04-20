from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        self.head = None
        self.tail = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.size += 1
        self.add_to_tail(value)
        # if not self.head and not self.tail:
        #     self.head = node
        #     self.tail = node
        # else:
        #     node.prev = self.tail
        #     self.tail.next = node
        #     self.tail = node

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_from_head()
        # val = self.head.value
        # self.head.prev.next = None
        # self.head = self.head.prev
        # return val

    def len(self):
        return self.size
