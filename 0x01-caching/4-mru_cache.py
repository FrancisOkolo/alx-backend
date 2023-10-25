#!/usr/bin/python3
"""a class to implement MRU caching"""


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.load = deque()

    def put(self, key, item):
        """add an element while implement MRU caching algorithm"""
        if key and item:
            if key in self.cache_data:
                self.load.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.load.pop()
                del self.cache_data[popped]
                print("DISCARD: " + str(popped))
            self.load.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get the cache"""
        if key in self.cache_data:
            self.load.remove(key)
            self.load.append(key)
            return self.cache_data.get(key, None)
