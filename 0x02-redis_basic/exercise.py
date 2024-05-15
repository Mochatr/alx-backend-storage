#!/usr/bin/env python3
"""
Module that provides a Cache class
for storing and retrieving data using Redis.
"""

import redis
import uuid
import functools
from typing import Callable, Union


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


def replay(func: Callable):
    """
    Display the history of calls of a particular function

    Args:
      func (Callable): The function to replay call history for.
    """
    qualified_name = func.__qualname__
    cache_instance = func.__self__
    inputs = cache_instance._redis.lrange(f"{qualified_name}:inputs", 0, -1)
    outputs = cache_instance._redis.lrange(f"{qualified_name}:outputs", 0, -1)
    count = cache_instance._redis.get(f"count:{qualifies_name}").decode()

    print(f"{qualified_name} was called {count} times:")
    for input_str, output_str in zip(inputs, outputs):
        input_str = input_str.decode()
        output_str = output_str.decode()
        print(f"{qualified_name}{input_str} -> {output_str}")


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
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
