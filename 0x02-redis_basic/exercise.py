#!/usr/bin/env python3
"""
This module defines a Cache class with decorators to count method calls,
store the history of inputs and outputs, and replay the history of calls.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method.
    The count is stored in Redis using the method's qualified name as the key.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.
    Inputs are stored in a Redis list with the
    key "<method>:inputs" and outputs
    in a list with the key "<method>:outputs".
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls to a particular function.

    Args:
        method (Callable): The function whose history is to be replayed.
    """
    redis = method.__self__._redis
    qualname = method.__qualname__

    call_count = redis.get(qualname).decode("utf-8")
    print(f"{qualname} was called {call_count} times:")

    input_key = f"{qualname}:inputs"
    output_key = f"{qualname}:outputs"

    inputs = redis.lrange(input_key, 0, -1)
    outputs = redis.lrange(output_key, 0, -1)

    for input_, output in zip(inputs, outputs):
        input_ = input_.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{qualname}(*{input_}) -> {output}")


class Cache:
    """
    Cache class for storing data in Redis with a randomly generated key.
    """

    def __init__(self) -> None:
        """
        Initialize a new Cache instance.
        The Redis client is stored as a private variable and the database is
        flushed.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in
            Redis.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data stored in Redis using the given key. Optionally apply
        a transformation function `fn` to the data before returning it.

        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): The function to apply to the data.

        Returns:
            Union[str, bytes, int, float, None]: The data retrieved from Redis,
            possibly transformed by `fn`.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data as a string from Redis using the given key.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[str]: The data retrieved from Redis as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data as an integer from Redis using the given key.

        Args:
            key (str): The key under which the data is stored.

        Returns:
            Optional[int]: The data retrieved from Redis as an integer.
        """
        return self.get(key, lambda d: int(d))
