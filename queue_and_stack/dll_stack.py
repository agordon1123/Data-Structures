import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because we will have a reference to order
        self.storage = DoublyLinkedList()

    def push(self, value):
        
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 

        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
