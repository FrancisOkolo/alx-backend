#!/usr/bin/python
'''A class that implements LRU caching
'''


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Initializing'''

    def __init__(self):
        self.cache_data = {}
        self.record_cache = []
        super().__init__()

    def get(self, key):
        '''get the cache'''
        if key not in self.cache_data or key is None:
            return None
        self.record_cache.append(key)
        return self.cache_data[key]

    def put(self, key, item):
        '''add to the cache while implementing LRU'''
        if key is None or item is None:
            return None
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lst = [(keyy, itemm) for keyy, itemm in self.cache_data.items()]
            if lst[0][0] in self.record_cache:
                last_item = lst.pop(1)
            else:
                last_item = lst.pop(0)
            self.record_cache.clear()
            last_item = list({last_item[0]: last_item[1]})
            updated_dict = {ke: va for ke, va in lst}
            self.cache_data = updated_dict
            self.cache_data[key] = item
            print("DISCARD:", last_item[0])
        else:
            self.cache_data[key] = item
