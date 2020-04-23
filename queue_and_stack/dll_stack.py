from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()

        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.add_to_tail(value)

    def pop(self):
        if self.length == 0:
            return None
        return self.remove_from_tail()

    def len(self):
        return len(self)
