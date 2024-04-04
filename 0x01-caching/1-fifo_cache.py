#!/usr/bin/python3
"""
FIFOCache caching class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    basic caching models an object that allows storage and
    retrieval of items from a dictionary.
    Fifo caching system have limits, removes first put item
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
        """
        if key is None or item is None:
            return

        # remove first put item if size exceeded
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            first_key, _ = self.cache_data.popitem(False)
            print("DICARD: ", first_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache dictionary in self.cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
