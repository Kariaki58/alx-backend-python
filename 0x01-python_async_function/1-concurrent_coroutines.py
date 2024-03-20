#!/usr/bin/env python3
"""lets execute multiple coroutines at the same time"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n - return a sorted list of random data"""
    list_content = []
    for _ in range(n):
        value = await wait_random(max_delay)
        list_content.append(value)
    return sorted(list_content)
