#!/usr/bin/env python3
"""
Module that provides a Cache class
for storing and retrieving data using Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self):
        """
        Initialize the Cache object with a Redis
        client connection.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using
        a random key.

        Args:
          data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
          str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    cache = Cache()
    print("Storing data...")

    key = cache.store("Hello, Redis!")
    print(f"Data stored under the key: {key}")
