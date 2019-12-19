from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.entries = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            if self.storage[key]:
                # move current node to tail
                self.entries.move_to_end(self.storage[key])
                return self.storage[key].value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            # move to most recently used
            self.entries.move_to_end(self.storage[key])
            # update value
            self.entries.tail.value = value
            # update cache
            self.storage[key] = self.entries.tail

        else:
            if self.size == self.limit:
                # remove oldest from head
                old_key, old_value = self.entries.remove_from_head()
                # remove oldest from storage
                del self.storage[old_key]
                self.size -= 1
                # insert node to tail
                self.entries.add_to_tail(key, value)
                # add node to queue
                self.storage[key] = self.entries.tail
                self.size += 1
            else:
                # insert node to tail
                self.entries.add_to_tail(key, value)
                # add node to queue
                self.storage[key] = self.entries.tail
                self.size += 1
