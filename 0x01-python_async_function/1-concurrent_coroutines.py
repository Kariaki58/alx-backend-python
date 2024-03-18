#!/usr/bin/env python3
"""import modules"""
import asyncio
from typing import List
from random import randint
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n"""
    delay_list = []
    tasks = []

    async def execute_wait_random():
        nonlocal delay_list
        delay = await wait_random(max_delay)
        delay_list.append(delay)

    for _ in range(n):
        task = asyncio.create_task(execute_wait_random())
        tasks.append(task)

    await asyncio.gather(*tasks)

    return sorted(delay_list)
