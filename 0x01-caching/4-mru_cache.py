#!/usr/bin/python3
"""
MRUCache caching class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    basic caching models an object that allows storage and
    retrieval of items from a dictionary.
    Mru caching system have limits, removes most used item
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
            # remove most used item if size exceeded
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                most_key, _ = self.cache_data.popitem(False)
                print("DICARD:", most_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache dictionary in self.cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
