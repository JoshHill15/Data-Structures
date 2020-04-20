from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        self.head = None
        self.tail = None
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.size += 1
        self.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_from_tail()

    def len(self):
        return self.size
