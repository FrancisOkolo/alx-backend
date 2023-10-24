#!/usr/bin/python3
'''A class to 'put' and 'get' data in & out of cache
'''


from Basebase_caching import BaseCaching


class BasicCache(BaseCaching):
    '''initializing'''
    def __init__(self):
        self.cache_data = {}

    def put(self, key, item):
        '''add to the cache'''
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        '''return a value from cache'''
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
