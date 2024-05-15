#!/usr/bin/env python3
"""
Module that provides a Cache class
for storing and retrieving data using Redis.
"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times
    a method of the Cache class is called.

    Args:
      method (Callable): The Cache class method to be
                         decorated.

    Returns:
      Callable: The wrapped method with call counting
      functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"count:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


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

    @count_calls
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
    count = cache._redis.get("count:Cache.store")
    print(f"store method was called {count.decode() if count else 0} times")
