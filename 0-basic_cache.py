#!/usr/bin/python3
#from base_caching import BaseCaching

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache implements a simple caching system using a dictionary."""

    def put(self, key, item):
        """Adds an item to the cache.

        Args:
            key: The key to associate with the item.
            item: The item to store in the cache.

        If key or item is None, does nothing.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """

        return self.cache_data.get(key)
