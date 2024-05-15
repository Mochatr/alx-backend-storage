#!/usr/bin/env python3
"""
Module that provides a Cache class
for storing and retrieving data using Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None) -> Union[str, int, bytes, None]:
        """
        Retrieve data from Redis by key,
        optionally converting it using a function.

        Args:
          key (str): The key where the data is stored.
          fn (Callable[[bytes], Union[str, int]], optional): A function to convert the data returned from Redis.

        Returns:
          Union[str, int, bytes, None]: The data retrieved from Redis, potentially converted, or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
          key (str): The key where the data is stored.

        Returns:
          Optional[str]: The string data or None if the key does not exist.
        """
        return self.get(key, lambda x: x.decode())

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
          key (str): The key where the data is stored.

        Returns:
          Optional[int]: The integer data or None f the key does not exist.
        """
        return self.get(key, int)


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
            b"foo": None,
            123: int,
            "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value, f"Error for value {value} with key {key}"
        print(f"Passed for value {value}")
