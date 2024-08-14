#!/usr/bin/env python3
"""
This module defines a function to fetch and cache HTML content of a URL
with request count tracking and an expiration time.
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def cache_page(expiration: int = 10) -> Callable:
    """
    Decorator to cache the HTML content of a URL and track access counts.

    Args:
        expiration (int): The expiration time for the cached content in seconds

    Returns:
        Callable: The decorated function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cache_key = f"count:{url}"
            cached_content = r.get(cache_key)

            if cached_content:
                return cached_content.decode("utf-8")

            html_content = func(url)
            r.incr(cache_key)
            r.setex(cache_key, expiration, html_content)

            return html_content
        return wrapper
    return decorator


@cache_page()
def get_page(url: str) -> str:
    """
    Fetches the HTML content of the specified URL and caches it.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
