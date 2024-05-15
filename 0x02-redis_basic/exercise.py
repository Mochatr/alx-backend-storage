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

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    for methods.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))

        return result
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
    print(f"store method was called {cache._redis.get('count:Cache.store').decode()} times")
    print(f"Input history: {cache._redis.lrange('Cache.store:inputs', 0, -1)}")
    print(f"Output history: {cache._redis.lrange('Cache.store:outputs', 0, -1)}")
