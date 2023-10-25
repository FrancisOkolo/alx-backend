#!/usr/bin/python3
'''A class that implements FIFO caching
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Initializing'''
    def __init__(self):
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        '''add to the cache while implementing FIFO'''
        if key is None or item is None:
            return None
        elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lst = list(self.cache_data)
            first_item = lst.pop(0)
            updated_dict = dict(lst)
            self.cache_data = updated_dict
            self.cache_data[key] = item
            print("DISCARD: ", first_item[0])
        else:
            self.cache_data[key] = item

def get(self, key):
    '''get the cache'''
    if key not in self.cache_data or key is None:
        return None
    return self.cache_data[key]