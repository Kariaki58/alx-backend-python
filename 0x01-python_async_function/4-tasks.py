#!/usr/bin/env python3
"""lets execute multiple coroutines at the same time"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait n - return a sorted list of random data"""
    list_content = []
    for _ in range(n):
        value = await task_wait_random(max_delay)
        list_content.append(value)
    return sorted(list_content)
