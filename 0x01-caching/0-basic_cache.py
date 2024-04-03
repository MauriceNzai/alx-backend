#!/usr/bin/python3
"""
Basic caching class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic caching models an object that allows storage and
    retrieval of items from a dictionary.
    This caching system doesn’t have limit
    """
    def put(self, key, item):
        """
        adds item to the cache i.e. dictionary self.cache_data
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache dictionary in self.cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
