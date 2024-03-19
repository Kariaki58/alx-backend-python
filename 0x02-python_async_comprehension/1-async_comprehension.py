#!/usr/bin/env python3
"""typing moudles"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehensions"""
    random_n = [n async for n in async_generator()]
    return random_n
