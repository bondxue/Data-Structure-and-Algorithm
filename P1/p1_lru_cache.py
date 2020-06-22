from collections import OrderedDict
import logging


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity
        if capacity <= 0:
            msg = "Cannot have cache capacity of zero of less."
            logging.error(msg)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.capacity <= 0:
            msg = "LRU is has empty capacity."
            logging.error(msg)
        else:
            if key not in self.cache:
                return -1
            else:
                self.cache.move_to_end(key)
                return self.cache[key]

    def set(self, key, value):
        if self.capacity <= 0:
            msg = "LRU is has empty capacity."
            logging.error(msg)
        else:
            # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
            self.cache[key] = value
            self.cache.move_to_end(key)
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


# test cases
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# test 2
print('-' * 30)
our_new_cache = LRU_Cache(2)
our_new_cache.set(1, 1)
our_new_cache.set(2, 2)
our_new_cache.set(1, 10)
print(our_new_cache.get(1))  # return 10
print(our_new_cache.get(2))  # return 2

# extreme case test
print('-' * 30)
another_cache = LRU_Cache(0)  # logging error since cache cannot be empty
another_cache.set(1, 1)  # logging error since cache is empty
another_cache.get(1)  # logging error since cache is empty
