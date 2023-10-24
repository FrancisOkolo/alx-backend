#!/usr/bin/python3
'''A class to 'put' and 'get' data in & out of cache
'''


from Base import BaseCaching


class BasicCache(BaseCaching):
    '''initializing'''
    def __init__(self):
        super().self.cache_data = {}

    def put(self, key, item):
        '''add to the cache'''
        if self.key is None or self.item is None:
            return None
        self.cache_data[self.key] = self.item

    def get(self, key):
        '''return a value from cache'''
        if self.key not in self.cache_data or self.key is None:
            return None
        return self.cache_data[self.key]
