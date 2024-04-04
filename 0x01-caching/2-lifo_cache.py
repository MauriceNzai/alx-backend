#!/usr/bin/python3
"""
LIFOCache caching class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    basic caching models an object that allows storage and
    retrieval of items from a dictionary.
    Lifo caching system have limits, removes last put item
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
            # remove last put item if size exceeded
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DICARD:", last_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=True)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Gets an item from the cache dictionary in self.cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
