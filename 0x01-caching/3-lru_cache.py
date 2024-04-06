#!/usr/bin/python3
"""
LRUCache caching class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    basic caching models an object that allows storage and
    retrieval of items from a dictionary.
    Lru caching system have limits, removes least used item
    """

    def __init__(self):
        """
        initialier constractor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        adds item to the cache i.e. dictionary self.cache_data
        if max size reached discard last put item
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            # remove least used item if size exceeded
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                least_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", least_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache dictionary in self.cache_data
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
        """
        if key is None or key not in self.cache_data:
            return None
        # self.cache_data.get(key, last=False)
        return self.cache_data.get(key)
        """
